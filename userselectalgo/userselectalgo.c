#include <openssl/evp.h>
#include <openssl/err.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void handleErrors(void) {
    ERR_print_errors_fp(stderr);
    abort();
}

int encrypt(unsigned char *plaintext, int plaintext_len, unsigned char *key,
            unsigned char *iv, unsigned char *ciphertext, const char *cipherType) {
    EVP_CIPHER_CTX *ctx;
    const EVP_CIPHER *cipher;
    int len;
    int ciphertext_len;

    /* Create and initialise the context */
    if (!(ctx = EVP_CIPHER_CTX_new())) handleErrors();

    /* Get the cipher */
    cipher = EVP_get_cipherbyname(cipherType);
    if (!cipher) {
        fprintf(stderr, "Cipher %s not found.\n", cipherType);
        exit(1);
    }

    /* Initialise the encryption operation. */
    if (1 != EVP_EncryptInit_ex(ctx, cipher, NULL, key, iv))
        handleErrors();

    /* Provide the message to be encrypted, and obtain the encrypted output. */
    if (1 != EVP_EncryptUpdate(ctx, ciphertext, &len, plaintext, plaintext_len))
        handleErrors();
    ciphertext_len = len;

    /* Finalise the encryption. */
    if (1 != EVP_EncryptFinal_ex(ctx, ciphertext + len, &len)) handleErrors();
    ciphertext_len += len;

    /* Clean up */
    EVP_CIPHER_CTX_free(ctx);

    return ciphertext_len;
}

int main(int argc, char *argv[]) {  
    if (argc != 6) {
        printf("Usage: %s <input file> <key> <IV> <output file> <algorithm>\n", argv[0]);
        return 1;
    }

    /* Load the human readable error strings for libcrypto */
    ERR_load_crypto_strings();

    /* Load all digest and cipher algorithms */
    OpenSSL_add_all_algorithms();

    FILE *fIn = fopen(argv[1], "rb");
    if (!fIn) {
        perror("Opening input file");
        return 1;
    }

    unsigned char key[EVP_MAX_KEY_LENGTH], iv[EVP_MAX_IV_LENGTH];
    strncpy((char *)key, argv[2], EVP_MAX_KEY_LENGTH);
    strncpy((char *)iv, argv[3], EVP_MAX_IV_LENGTH);

    fseek(fIn, 0, SEEK_END);
    long fSize = ftell(fIn);
    fseek(fIn, 0, SEEK_SET);

    unsigned char *plaintext = malloc(fSize + 1);
    fread(plaintext, 1, fSize, fIn);
    fclose(fIn);

    unsigned char *ciphertext = malloc(fSize + EVP_MAX_BLOCK_LENGTH);

    int ciphertext_len = encrypt(plaintext, fSize, key, iv, ciphertext, argv[5]);

    FILE *fOut = fopen(argv[4], "wb");
    if (!fOut) {
        perror("Opening output file");
        return 1;
    }

    fwrite(ciphertext, 1, ciphertext_len, fOut);
    fclose(fOut);

    free(plaintext);
    free(ciphertext);

    /* Clean up */
    EVP_cleanup();
    ERR_free_strings();

    return 0;
}

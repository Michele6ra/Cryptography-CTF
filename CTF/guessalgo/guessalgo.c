#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>

#define ENCRYPT 1
#define DECRYPT 0

int main()
{
    unsigned char key_c[] = "0123456789ABCDEF";
    unsigned char iv_c[] = "0123456789ABCDEF";
    unsigned char ciphertext_hex[]  = "65927e04a24d7695c0da367f1983922d46895ad7c86279306f1f03ff513ef8";
    unsigned char ciphertext_hex1[] = "65927e04a24d7695c0da397f1983922d46895ad7c862f79306f1f03ff513ef8";
    unsigned char ciphertext_hex2[] = "65927e04a24d7695c0da3697f1983922d46895ad7c862f79306f1f03ff513ef8";


    unsigned char key[]="d35db7e39ebbf3d001083105";
    unsigned char iv[]="d35db7e39ebbf3d001083105";


    /*for (int i = 0; key_c[i] != '\0'; i++) {
        sscanf(&key_c[i], "%02x", &key[i]);
        sscanf(&key_c[i], "%02x", &iv[i]);
    }*/

    unsigned char key_bin[strlen(key)/2];
    unsigned char iv_bin[strlen(iv)/2];
    for(int i = 0; i < strlen(key)/2;i++){
        sscanf(&key[2*i],"%2hhx", &key_bin[i]);
        sscanf(&iv[2*i],"%2hhx", &iv_bin[i]);
    }

    



    FILE *f_in1;
    unsigned char buffer[1024];
    const EVP_CIPHER *cipher;
    int n=0;
    f_in1 = fopen("algo_list.txt", "r");
    while ((fgets(buffer, 1024, f_in1))!=NULL)
    {
        n=strlen(buffer);
        buffer[n-1]= '\0';
        EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
        EVP_CIPHER_CTX *ctx1 = EVP_CIPHER_CTX_new();
        EVP_CIPHER_CTX *ctx2 = EVP_CIPHER_CTX_new();
        cipher = EVP_get_cipherbyname(buffer);
        if (!cipher) {
        fprintf(stderr, "Cipher %s not found.\n", buffer);
        }

        

        EVP_CipherInit(ctx, cipher, key, iv, DECRYPT);
        EVP_CipherInit(ctx1, cipher, key, iv, DECRYPT);
        EVP_CipherInit(ctx2, cipher, key, iv, DECRYPT);

        // convert hexstring into bytes
        int ciphertext_len = strlen(ciphertext_hex) / 2;
        unsigned char ciphertext_binary[ciphertext_len];
        for (int i = 0; i < ciphertext_len; i++)
        {
            sscanf(&ciphertext_hex[2 * i], "%2hhx", &ciphertext_binary[i]);
        }

        int ciphertext_len1 = strlen(ciphertext_hex1) / 2;
        unsigned char ciphertext_binary1[ciphertext_len1];
        for (int i = 0; i < ciphertext_len1; i++)
        {
            sscanf(&ciphertext_hex1[2 * i], "%2hhx", &ciphertext_binary1[i]);
        }

        int ciphertext_len2 = strlen(ciphertext_hex2) / 2;
        unsigned char ciphertext_binary2[ciphertext_len2];
        for (int i = 0; i < ciphertext_len2; i++)
        {
            sscanf(&ciphertext_hex2[2 * i], "%2hhx", &ciphertext_binary2[i]);
        }

        unsigned char decrypted[ciphertext_len]; // may be larger than needed due to padding
        unsigned char decrypted1[ciphertext_len1];
        unsigned char decrypted2[ciphertext_len2];

        int update_len, final_len;
        int decrypted_len = 0;
        EVP_CipherUpdate(ctx, decrypted, &update_len, ciphertext_binary, ciphertext_len);
        decrypted_len += update_len;

        EVP_CipherFinal_ex(ctx, decrypted + decrypted_len, &final_len);
        decrypted_len += final_len;
        printf("---------> %s\n", decrypted);

        EVP_CIPHER_CTX_free(ctx);

        printf("Plaintext length = %d\n", decrypted_len);
        for (int i = 0; i < decrypted_len; i++)
            printf("%02x", decrypted[i]);
        printf("\n");
        for (int i = 0; i < decrypted_len; i++)
            printf("%c", decrypted[i]);
        printf("\n");


        //--------------------

        int update_len1, final_len1;
        int decrypted_len1 = 0;
        EVP_CipherUpdate(ctx1, decrypted1, &update_len1, ciphertext_binary1, ciphertext_len1);
        decrypted_len1 += update_len1;

        EVP_CipherFinal_ex(ctx1, decrypted1 + decrypted_len1, &final_len1);
        decrypted_len1 += final_len1;
        printf("1---------> %s\n", decrypted1);

        EVP_CIPHER_CTX_free(ctx1);

        printf("Plaintext length1 = %d\n", decrypted_len1);
        for (int i = 0; i < decrypted_len1; i++)
            printf("%02x", decrypted1[i]);
        printf("\n");
        for (int i = 0; i < decrypted_len1; i++)
            printf("%c", decrypted1[i]);
        printf("\n");

        //--------------------------

        int update_len2, final_len2;
        int decrypted_len2 = 0;
        EVP_CipherUpdate(ctx2, decrypted2, &update_len2, ciphertext_binary2, ciphertext_len2);
        decrypted_len2 += update_len2;

        EVP_CipherFinal_ex(ctx2, decrypted2 + decrypted_len2, &final_len2);
        decrypted_len2 += final_len2;
        printf("2---------> %s\n", decrypted2);

        EVP_CIPHER_CTX_free(ctx2);

        printf("Plaintext length2 = %d\n", decrypted_len2);
        for (int i = 0; i < decrypted_len2; i++)
            printf("%02x", decrypted2[i]);
        printf("\n");
        for (int i = 0; i < decrypted_len2; i++)
            printf("%c", decrypted2[i]);
        printf("\n");

        //------------------------

        printf("\n");
        printf("\n");
        printf("--------------------------------------------");
        printf("%s", buffer);
        printf("--------------------------------------------");
        printf("\n");
        printf("\n");
    }

    return 0;
}
#include <stdio.h>
#include <string.h>

#include <openssl/evp.h>


#define ENCRYPT 1
#define DECRYPT 0

int main()
{

//int EVP_EncryptInit(EVP_CIPHER_CTX *ctx, const EVP_CIPHER *type, const unsigned char *key, const unsigned char *iv);
//int EVP_EncryptFinal(EVP_CIPHER_CTX *ctx, unsigned char *out, int *outl);

//  int EVP_DecryptInit(EVP_CIPHER_CTX *ctx, const EVP_CIPHER *type, const unsigned char *key, const unsigned char *iv);
//  int EVP_DecryptFinal(EVP_CIPHER_CTX *ctx, unsigned char *outm, int *outl);

//  int EVP_CipherInit(EVP_CIPHER_CTX *ctx, const EVP_CIPHER *type, const unsigned char *key, const unsigned char *iv, int enc);
//  int EVP_CipherFinal(EVP_CIPHER_CTX *ctx, unsigned char *outm, int *outl);




    

    unsigned char key[] = "0123456789ABCDEF";
    unsigned char iv[]  = "0123456789ABCDEF";
    unsigned char ciphertext_hex[] = "65927e04a24d7695c0da3697f1983922d46895ad7c862f79306f1f03ff513ef8";
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
        cipher = EVP_get_cipherbyname(buffer);
        if (!cipher) {
        fprintf(stderr, "Cipher %s not found.\n", buffer);
        }
        EVP_CipherInit(ctx, cipher, key, iv, DECRYPT);
        
        // convert hexstring into bytes
        int ciphertext_len = strlen(ciphertext_hex)/2;
        unsigned char ciphertext_binary[ciphertext_len];
        for(int i = 0; i < ciphertext_len;i++){
            sscanf(&ciphertext_hex[2*i],"%2hhx", &ciphertext_binary[i]);
        }
        for(int i = 0; i < ciphertext_len; i++)
            printf("%02x", ciphertext_binary[i]);
        printf("\n");


        unsigned char decrypted[ciphertext_len]; //may be larger than needed due to padding

        int update_len, final_len;
        int decrypted_len=0;
        EVP_CipherUpdate(ctx,decrypted,&update_len,ciphertext_binary,ciphertext_len);
        decrypted_len+=update_len;
        printf("update size: %d\n",decrypted_len);

        EVP_CipherFinal_ex(ctx,decrypted+decrypted_len,&final_len);
        decrypted_len+=final_len;
        printf("---------> %s\n", decrypted);

        EVP_CIPHER_CTX_free(ctx);

        printf("Plaintext lenght = %d\n",decrypted_len);
        for(int i = 0; i < decrypted_len; i++)
            printf("%2x", decrypted[i]);
        printf("\n");
        for(int i = 0; i < decrypted_len; i++)
            printf("%c", decrypted[i]);
        printf("\n");
        printf("\n");
        printf("\n");
        printf("--------------------------------------------\n");
        printf("----------------->>>>>>>>%s\n", decrypted);
        printf("%s\n", cipher);
        printf("--------------------------------------------\n");
        printf("\n");
        printf("\n");
        
        }


        return 0;
}
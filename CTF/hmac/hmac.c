#include <stdio.h>
#include <openssl/evp.h>
#include <openssl/hmac.h>
#include <openssl/err.h>
#include <string.h>

int main(int argc, char **argv){

    ERR_load_crypto_strings();
    OpenSSL_add_all_algorithms();


    unsigned char key[] = "keykeykeykeykeykey";
    FILE *f_in1;
    FILE *f_in2;
    if((f_in1 = fopen(argv[1],"r")) == NULL) {
            fprintf(stderr,"Couldn't open the input file, try again\n");
            exit(1);
    }
    if((f_in2 = fopen(argv[2],"r")) == NULL) {
            fprintf(stderr,"Couldn't open the input file, try again\n");
            exit(1);
    }
    EVP_MD_CTX  *hmac_ctx = EVP_MD_CTX_new();

    EVP_PKEY *hkey;
    hkey = EVP_PKEY_new_mac_key(EVP_PKEY_HMAC, NULL, key, 18);

    EVP_DigestSignInit(hmac_ctx, NULL, EVP_sha256(), NULL, hkey);


    int n;
    unsigned char buffer[1024];
    while((n = fread(buffer,1,1024,f_in1)) > 0){
        // Returns 1 for success and 0 for failure.
            EVP_DigestSignUpdate(hmac_ctx, buffer, n);                
        }
    while((n = fread(buffer,1,1024,f_in2)) > 0){
        // Returns 1 for success and 0 for failure.
        EVP_DigestSignUpdate(hmac_ctx, buffer, n);
    }
    

    unsigned char hmac_value[EVP_MD_size(EVP_sha256())];
    size_t hmac_len = EVP_MD_size(EVP_sha256());
    EVP_DigestSignFinal(hmac_ctx, hmac_value, &hmac_len);

    for(int i = 0; i < hmac_len; i++)
			     printf("%02x", hmac_value[i]);
}


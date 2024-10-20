#include <stdio.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <string.h>

//kd = SHA512 ( secret || input_file || secret)

int main(int argc, char *argv[]){
    unsigned char secret[] = "this_is_my_secret";
    FILE *f_in;
    if((f_in = fopen(argv[1],"r")) == NULL) {
            fprintf(stderr,"Couldn't open the input file, try again\n");
            exit(1);
    }

    EVP_MD_CTX *md = EVP_MD_CTX_new();

    EVP_DigestInit(md, EVP_sha512());

    size_t n_read;
    unsigned char buffer[1024];
    EVP_DigestUpdate(md, secret, strlen(secret));
    while((n_read = fread(buffer,1,1024,f_in)) > 0){
    // Returns 1 for success and 0 for failure.
        EVP_DigestUpdate(md, buffer, n_read);

    }
    EVP_DigestUpdate(md, secret, strlen(secret));

    unsigned char md_value[EVP_MD_size(EVP_sha512())];
    int md_len;
    EVP_DigestFinal_ex(md, md_value, &md_len);
    for(int i=0; i<md_len; i++){
        printf("%02x", md_value[i]);
    }







}
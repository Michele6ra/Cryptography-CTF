

/*
#include <stdio.h>
#include <string.h>

#include <openssl/evp.h>
int main(){
    printf("------------");

    unsigned char rand1 [] = "63-3b-6d-07-65-1a-09-31-7a-4f-b4-aa-ef-3f-7a-55-d0-33-93-52-1e-81-fb-63-11-26-ed-9e-8e-a7-10-f6-63-9d-eb-92-90-eb-76-0b-90-5a-eb-b4-75-d3-a1-cf-d2-91-39-c1-89-32-84-22-12-4e-77-57-4d-25-85-98";
    unsigned char rand2 [] = "92-05-d8-b5-fa-85-97-b6-22-f4-bd-26-11-cf-79-8c-db-4a-28-27-bb-d3-31-56-74-16-df-cb-f5-61-a7-9d-18-c2-63-92-f1-cb-c3-6d-2b-77-19-aa-21-07-8e-fe-8b-1a-4f-7d-70-6e-a4-7b-c8-68-30-43-12-50-30-1e";
    int rand1_len= strlen(rand1);
    unsigned char rand1_pulita[rand1_len];
    unsigned char rand2_pulita[rand1_len];    
    unsigned char rand1_bin [rand1_len];
    unsigned char rand2_bin [rand1_len];

    unsigned char k1 [rand1_len];
    unsigned char k2 [rand1_len];
    unsigned char flag [rand1_len];

    printf("------------\n");

    for(int i = 0; i < rand1_len;i++){
        //printf("%c \n", rand1[i]);
        if (rand1[i]!='-'){
            sscanf(&rand1[i],"%c", &rand1_pulita[i]);
            //printf("%c \n", rand1_pulita[i]);
            sscanf(&rand2[i],"%c", &rand2_pulita[i]);

        }
    }
    for (int i=0; i< rand1_len/2; i++){
        printf("\nrand1 :");
        printf("%02x ", rand1_pulita[i*2]  );
        printf("\nrand2 :");
        printf("%02x ", rand2_pulita[i*2]  );

    }
    

    int rand1_pulita_len= strlen(rand1_pulita)/2;
    
    for(int i = 0; i < rand1_pulita_len; i++){
        sscanf(&rand1_pulita[2*i],"%2hhx", &rand1_bin[i]);
        sscanf(&rand2_pulita[2*i],"%2hhx", &rand2_bin[i]);

    }
    printf("------------\n");

    for (int i=0; i<rand1_pulita_len; i++){
        k1[i] = rand1_bin[i] | rand2_bin[i];
        k2[i] = rand1_bin[i] & rand2_bin[i];
        flag[i] = k1[i] ^ k2[i];

        printf("%2x", flag[i]);
    }




}*/
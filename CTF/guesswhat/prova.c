#include <stdio.h>
#include <openssl/bn.h>

int main ()
{
  BN_CTX *ctx=BN_CTX_new();

  BIGNUM *a = BN_new();
  BIGNUM *b = BN_new();
  BIGNUM *c = BN_new();
  BIGNUM *r = BN_new();
  char hex_string1[] = "00000000000000000000000000009eee82dc2cd4a00c4f5a7b8663b0c1ed0677fcebde1a235df4c3ff876a7dadc607faa835f6ae0503573e223676d50d574f99f958ad637ae745a6aafa023423b69d34157b1141b6b1cab91acd2955bd42f504abdf454a9d4eca4e01f9f8745967eeb6a9fb96b7c09400178a530eb6d831c968e66438d3633a04d7886bf0e1ad607f41bd857bd904e1975b1f9b05ceac2cc4553fb48b894d0a509a094e5e8f5b5f5569725f049b3a8a09b47f8db2ca520e5ebff4b0eec9badc934f6dd31f821ad9fc2ca73f18230dd744c728546784ee739265f01ce81e6d4d9565b4c84fb80462582bee3264a0a7dc99250e505376bc30db715e93d69f1f881c765d82c8593951";
  char hex_string2[] = "000000000000000d2c601326b4c4b855f527bb78ed68ae4c8767e6bc9249a3ecacd2fc9b875d4f97111e1cfbe62d32c5ff9fd9bfaed62f3df44c757fbee9bb232cb5449296c692e301d8c1ffab18ee44966c1fb927c82ca60c940a40ab2db50ecf6ff98a71623388d06d27ca9858ac22b4dd4e6f189e5b04254a05f3cddc764330511fbee8b2607";
  char hex_string3[] = "00C108C95709E073727DB45E4B4B20BF3C5741BF5CBC144DA66ABD4D8669069F739D402C600F297B0B4CC77BF65EE5A61002713E74A5ACB97FF3C57842CAFE506F5B1BDFC7EE3620BB5673AB11FAE2BFA8697DE6F45C27C121693C0E1D2DDD702511579F8A5A605809905C54E0552A551CE1369D1470ABB4E2CEC4926BFA148FE7";
  BN_hex2bn(&a, hex_string1);
  BN_hex2bn(&b, hex_string2);
  BN_hex2bn(&c, hex_string3);
  

  BN_add(r, a, b);
  printf("risultato somma -----\n");
  BN_print_fp(stdout, r);
  printf("\n");
  BN_sub(r,a, b);
  printf("risultato sottrazione -----\n");
  BN_print_fp(stdout, r);
    printf("\n");
  BN_mul(r, c, b,ctx);
  printf("risultato moltiplicazione-----\n");
  BN_print_fp(stdout, r);
    printf("\n");
    BIGNUM *dv = BN_new();
    BIGNUM *rem = BN_new();
  BN_div(dv, rem, a,b, ctx);
  printf("risultato divisione -----\n");
  BN_print_fp(stdout, dv);
  printf("\n");
  BN_print_fp(stdout, rem);


  



  return 0;
}
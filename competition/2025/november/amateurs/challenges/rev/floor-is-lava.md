---
type: challenge
event: amateurs
name: floor-is-lava
category: rev
note: "[[ELF x86-64]]"
solved: ✅
---




| Variable | Address    |
| -------- | ---------- |
| ii       | 0x00104051 |
| jj       | 0x00104050 |
| arr      | 0x00104010 |
| counter  | 0x00104038 |
```cpp
  while (local_28 < 0x1c) {
    printf("> ");
    do {
      iVar5 = getchar();
      cVar3 = (char)iVar5;
    } while (cVar3 == '\n');
    if (cVar3 == 'w') {
      ii = ii - 1;
      puVar2 = PTR_DAT_00104038 + 1;
      *PTR_DAT_00104038 = 0;
      PTR_DAT_00104038 = puVar2;
      goto LAB_001012eb;
    }
    if (cVar3 == 'a') {
      jj = jj - 1;
      puVar2 = PTR_DAT_00104038 + 1;
      *PTR_DAT_00104038 = 1;
      PTR_DAT_00104038 = puVar2;
      goto LAB_001012eb;
    }
    if (cVar3 == 's') {
      ii = ii + 1;
      puVar2 = PTR_DAT_00104038 + 1;
      *PTR_DAT_00104038 = 2;
      PTR_DAT_00104038 = puVar2;
      goto LAB_001012eb;
    }
    if (cVar3 == 'd') {
      jj = jj + 1;
      puVar2 = PTR_DAT_00104038 + 1;
      *PTR_DAT_00104038 = 3;
      PTR_DAT_00104038 = puVar2;
    }
    jj = jj & 7;
	ii = ii & 7;
      (&DAT_00104010)[(int)(uint)ii] = (&DAT_00104010)[(int)(uint)ii] ^ (byte)(1 << jj);
      local_28 = local_28 + 1;
  }
```

We want `DAT_00104010` to equal:
```cpp
    srand(local_24 * 0x1337 + 0xdeadbeef);
    uVar4 = rand();
    if ((uVar4 & 0xff) != (uint)(byte)(&DAT_00104010)[local_24]) {
      puts("you fell into lava");
      goto LAB_001014a5;
    }
    local_24 = local_24 + 1;
```
So we can just create the array to make it equal:
```cpp
#include <bits/stdc++.h>
using namespace std;

unsigned arr[20];
unsigned current[] = {0x8b, 0xc9, 0x92, 0x08, 0xf9, 0x91, 0xd6, 0xc8};

int main() {
  int cnt = 0;
  for (int i = 0; i < 8; i++) {
    srand(i * 0x1337 + 0xdeadbeef);
    arr[i] = rand() & 0xff;
    arr[i] ^= current[i];
    cnt += __builtin_popcount(arr[i]);

    for (int j = 0; j < 8; j++) {
      cout << ((arr[i] >> j) & 1);
    }
    cout << '\n';
  }
  cout << cnt << endl;
}
// dsddwwawddwddwwddsdddwdwdwwd
```


---
type: challenge
event: csaw qual
name: Rock
category: rev
note: "[[ELF x86-64]]"
solved: ✅
---
```cpp
class DarkTemplar{
public:
  virtual int getSerial() = 0;
};

class HighTemplar: public DarkTemplar{
public:
  HighTemplar(const string& solution) : solution(solution),rock_flag(solution){}

  void calculate(){
    if (solution.length() != 30){
      cout << "Too short or too long" << endl;
      exit(-1);
    }

    for(int i =0;i <= solution.length();i++){
        solution[i] = char((solution[i]^0x50)+(20%25));
    }

    for(int i =0; i <= solution.length();i++){
        solution[i] = char((solution[i] ^ 0x10)+(265%999));
    }
  }

  int getSerial(){
    for(int i = 0;i< solution.length();i++){
      if (answer[i] == solution[i]){
        cout << "Pass " << i  << endl;  
      }else{
        cout << "You did not pass " << i << endl;
        flag = 1;
        break;
      }
    }
    return flag;
  }

  string getFlag(){
    return rock_flag;
  }

private:
  int value; // 0x8
  int flag = 0; // 0xc
  string solution; // 0x10
  string rock_flag; // 0x18
  string answer = "FLAG23456912365453475897834567"; // 0x20

};
```

Memory layout of `HighTemplar`
```
HighTemplar object
+0x00   vptr
+0x08   int value
+0x0C   int flag
+0x10   char* solution
+0x18   char* rock_flag
+0x20   char* answer
--------------------------------
Total so far: 0x28 (40 bytes)
```



```cpp
struct Node{
public:
  Node(const char& character) : str(character){}

  char str; // 0x1
  Node* prev; // 0x8
  Node *next; // 0x10

};
```

Memory layout of `Node`
```
Offset  Size   Member
---------------------------------
0x00     1     char str
0x01     7     padding (to align next pointer)
0x08     8     Node* prev
0x10     8     Node* next
---------------------------------
Total size: 0x18 bytes (24 bytes)
```
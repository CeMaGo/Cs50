# CS50 Fall 2023 Week 5 Data Structures 

## Live Lecture on Youtube 11.Oct.2023 7:30 pm Berlin Germany

---

### queues

 - [ ] FiFo (first in, first, out)
   - [ ] enqueue
   - [ ] dequeue

```C
 const int CAPACITY = 50 

 typedef struct
 {
    person people[CAPACITY];
    int size
 }
queue;
```

---

### Stacks

 - [ ] LIFO (Last in, First Out)
   - [ ] Push
   - [ ] Pop


```C
 const int CAPACITY = 50 

 typedef struct
 {
    person people[CAPACITY];
    int size
 } 
stack;
```

---

### arrays

> 💡 stores data contiguously , back to back to back

```C
#include <stdio.h>

int main(void)
{
    int *list = malloc(3 * size0f(int));
    if (list == NULL)
    {
        return 1
        };

list[0] = 1:
list[1] = 2;
list[2] = 3;


int *tmp = malloc(4 * sizeof(int));
if (temp == NULL)
{
    free(list);
    return 1;
}


for( int i = 0; i < 3; i++)
{
    temp[i] = list[i]:
}
tmp[3] = 4;

free(list)
list = tmp;


for(int i = 0; i < 3; i++)
{
    printf("%i\n", list[i])
}
}
```

---

### struct 

 `.`  go into
 `*` point at  
 `->` go into ...

---

## linked lists

- [ ] located somewhere in memory but linked by pointers. we can locate at random location as long as we link the chucks with pointers.

- [ ] trade off is gonna be space, or time. twice as much space (one for data + address to the next location)


Node1 = 1 0x123, + (location for the next item) 0x456
Node 2 =2 0x456,  + (location for the next item) 0x789
Node 3 =3 0x789,  + (location for the next item) NULL

`Meta-data` is the extra Pointer, value + meta- data 


``` C
typedef struct
{
    string name;
    string number;
} person;

typedef struct
{
    char* name;
    char *number;
} person;

typedef struct node
{
    int number;
    node *next
} node

// note top to bottom read `node` has to be mentioned before it returns and is usable
```

```C
node *list = NULL;
// set it NULL!!!

node *n = malloc(sizeof(node));


(*n).number = 1; // star `n` pointer, `.dot` go in, `=` assign 1
n -> number = 1 // does the same just nicer syntax

list = n ;

node *n = malloc(sizeof(2))

n -> number = 2
n -> next = list
list = n;

//oder of oporations matter to not loose data
```


 ```c
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;

}node

int main ( int argc , char* argv[])
{
    node *list =Null;

     (for i = 1; i< argc; i++>)
    {
        int number = atoi(argv[i];
        
        node *n = malloc *sizeof(node));
        if (n== NULL)
{
    // free memory thus fR
   return 1;
}        
     {
        printf("%i\n",argv[i])
     }   
    }


n -> number= number;
n -> next = list;
list =n  -->


// print whole list 
node *ptr = list;
while (ptr !=NULL){
}
printf("i%\n", ptr ->number 
ptr = ptr -> next;)
}
// run time how much does it cost to insert into a linked list (prepend, prepend) O(1)/ constant time! `O of 1`, searching run time: O(n) / as many items as in the list, each hast to be checked.
// Binary search does not work on Linked list?
// what do you need, time efficient, quality of design etc

```


NEED TO REVIEW AND COPPY CODE AGAIN
 about 70 min in

 ---
 ---

 ## trees

 big o of log n | O(log n)

 - [ ] Binary search trees 

 [1] | [2] | [3] | [4] | [5] | [6] | [7]
                   / \
        |                       |
       [2]                     [6]
       / \                     / \
     [1] [3]                 [5] [7]

``` c
    typedef struct node
    {
        int number;
        struct 
    }

    bool search(node *tree, int number)
    {
        if( tree== Null)
        {
            return false;
        }
        else if (number < tree -> number)
        {
            return search(tree -> left, number)
        }
        else if (number > tree -> number)
        {
            return search(tree ->number)
        }
        else
        
        
            }

```


### dictionaries

 - [ ] keys and values

 in this example names are the keys and numbers the value, we are building a phonebook...

 at best in bianry search we would like O(log n) or even better ! constant time, indipedent of N, the ultimate goal

 ### hashing

  - [ ] what is a hash function,  hash value, hash table

- takes inputs and hashes them to input values

> hash function is a map function that takes as input and outputs a value
> hash table name | numbers .. 

phonebook 26 

1/A [ ]
2/B [ ]
3/C [ ]
...
/L [ ] Luigi, -> Lucas, ->

pointer to linked list

(think of javascript objects, key + linked list)

in the worst case linkedlist is big O of n

// instead of storing just the first letter , i get a bigger bucket 
// sacrificing memory
// obtain the holy grail of constant time...

typedef struct node
{
char *name
char *number;
struct node *next 
}
node

node* table[26]; // hashtable 

input hash -function
value look at hash-value
output hash-table


``` c
include <ctype.h>

int hash(const char *word) // unchangeable word `const`, defend your code 
{
    return toupper(word[0]) - 'A';
}
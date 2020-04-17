#include <stdio.h>

typedef struct FIFO{ // type: 1 = int, 2: pair of int, 3:float, 4:string,
    int first;
    int second;
    float number;
    char string[100];
    int type;
};

struct FIFO queue[3];
int counter = 0;
int last_in_queue = 0;
int first_in_queue = 0;
int struct_size = 3;

void push()
{
    if (counter == struct_size)
    {
        printf("Przepełniono kolejke - brak możliwości dodania\n");
    }
    else
    {
        int start_size = counter;
        int type;
        printf("wybierz opcje dodania: \n");
        printf("1: liczba, 2: para liczb, 3: liczba zmiennoprzecinkowa, 4: napis (maksymalnie 100 znaków) \n" );
        int option;
        scanf("%d", &option);
        if(option == 1)
        {
            printf("Podaj liczbę całkowitą\n");
            int tmp;
            scanf("%d", &tmp);
            queue[last_in_queue].first = tmp;
            queue[last_in_queue].type = 1;
            counter++;

        }
        else
        {
            if(option == 2)
            {
                printf("Podaj pierwszą liczbę\n");
                int tmp;
                int tmp1;
                scanf("%d", &tmp);
                printf("Podaj drugą liczbę\n");
                scanf("%d", &tmp1);
                queue[last_in_queue].first = tmp;
                queue[last_in_queue].second = tmp1;
                queue[last_in_queue].type = 2;
                counter++;
            }
            else
            {
                if(option == 3)
                {
                    printf("Podaj liczbę\n");
                    float tmp;
                    scanf("%f", &tmp);
                    queue[last_in_queue].number=tmp;
                    queue[last_in_queue].type = 3;
                    counter++;
                }
                else
                {
                    if(option == 4)
                    {
                        char tmp[100];
                        scanf("%s", tmp);
                        for(int i=0; i <100; i++){
                          queue[last_in_queue].string[i]=tmp[i];
                        }
                        queue[last_in_queue].type = 4;
                        counter++;
                    }
                    else{
                    printf("Podano złą wartość\n");
                    }

                }
            }
        }
        if(start_size<counter)
        {
            last_in_queue++;
            last_in_queue = last_in_queue % struct_size;
        }
    }
}


void pop()
{
    if (counter == 0)
    {
        printf("Kolejka pusta - nie można z niej wyjąć");
    }
    else
    {
        if(queue[first_in_queue].type==1)
        {
            printf("Usunięto liczbę całkowitą ");
            printf("%d", queue[first_in_queue].first);

        }
        else
        {
            if(queue[first_in_queue].type==2)
            {
                printf("Usunięto dwie liczby całkowite ");
                printf("%d", queue[first_in_queue].first);
                printf(" ");
                printf("%d", queue[first_in_queue].second);
            }
            else
            {
                if(queue[first_in_queue].type == 3)
                {
                    printf("Usunięto liczbę zmiennoprzecinkową ");
                    printf("%f", queue[first_in_queue].number);
                }
                else
                {
                    if (queue[first_in_queue].type == 4)
                    {
                        printf("Usunięto napis ");
                        printf("%s",queue[first_in_queue].string);

                    }
                    else{
                        printf("wybrano złą opcje");
                    }
                }
            }
        }
        printf("\n");
        counter--;
        first_in_queue++;
        first_in_queue = first_in_queue % struct_size;
    }
}


int main()
{
    while(1)
    {
        printf("wybierz opcje: 1 dodanie elementu, 2 usunięcie elementu \n");
        int option;
        scanf("%d",&option);
        if(option == 1){
            push();
        }
        else
        {
            if(option == 2){
                pop();
            }
             else{
                 printf("błędna opcja: wybierz ponownie");
             }
        }

    }
    return 0;
}






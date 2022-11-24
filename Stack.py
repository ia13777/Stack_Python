                                #Stack Data Structure

    #Container(Array)
container = [];
    #Pointer
InitialPointer=-1;
ActualPointer=int;

    #Data storing functions (add,remove,container full,container empty)

#Adding Data to container
def add(data) :
    #data input variable
    container.append(data);

    #printing status
    print("data ", data, " added");

    return None;

#checking out pointer position
def pointercheck() :
    ActualPointer=len(container)-1;
    print("pointer index position :", ActualPointer);
    return None;

#checking empty status
def IsEmpty():
    ActualPointer=len(container)-1;
    status=bool;
    if ActualPointer == InitialPointer :
        status=True;
        print(status)
    else :
        status=False;
        print(status)
    return None;

#removing data from container
def remove():
    ActualPointer = len(container)-1;
    container.remove(container[ActualPointer]);
    print('data removed');
    return None;


#data entry
add('i');

add('r');

add('v');

add('i');

add('n');

add('g');

print(' \n ');

print(container);


#data searching function

#name reverse
def reverseName():
    print('reverse name :');
    #actual stack pointer(stack method)
    ActualPointer = len(container)-1;
    #new container
    reverseContainer = [];
    while ActualPointer > InitialPointer :
        #adding element to new container
        reverseContainer.append(container[ActualPointer]);
        #pointer moves
        ActualPointer = ActualPointer-1;

    print(reverseContainer);


#searching program

reverseName();







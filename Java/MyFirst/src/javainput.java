import java.util.*;


public class javainput {
    public static void main(String[] args) {
        // we are taking input from input window
        Scanner sc= new Scanner(System.in);
        // sc acts as object here 
        // we need to store input in some variable:
        // next() is a method in sc object which takes only single token
        // String name = sc.next();
        // to take whole line as input we need to use nextLine() method:
        String name = sc.nextLine();
        // nextInt() to take integer as input
        // nextFloat() to take float as input
        // nextDouble() to take double as input
        System.out.println("Hi my name is " + name);
    }
    
}

public class ComputorV1{
    static String equation;

    public static void main(String[] args) {
        try {
            equation = "";
            if(args.length != 1)
            {
                System.out.println("Equation must only be one argument");
                return ;
            }
            else 
            {
                equation = args[0];
            }
        }
        catch(Exception e)
        {
            System.out.println("Please enter an equation");
        }

        try
        {
            Functions newEq = new Functions(equation);
            newEq.Calculation();
        }
        catch (Exception e)
        {
            System.out.println("Equation not solved, Try again!!! ");
        }
    }
}
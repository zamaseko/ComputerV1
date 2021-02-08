package comp;

import java.util.ArrayList;
import java.util.*;
import java.util.List;

public class ComputorV1
{
    public static float poly_deg = 0;
    public static float discriminant;
    public static void main(String []args) {
        if(args.length != 1)
        {
            System.out.println("There must only be one argument");
            System.exit(1);
        }
        String formula[] = args[0].split("=");
        System.out.println(formula[1]);
        String ls[] = formula[0].split(" ");
        String rs[] = formula[1].split(" ");
        // String lhs[] = new String[ls.length];
        // String rhs[] = new String[rs.length];
        List<String> lhs = new ArrayList<String>();
        List<String> rhs = new ArrayList<String>();
        List<String> deg0 = new ArrayList<String>();
        List<String> deg1 = new ArrayList<String>();
        List<String> deg2 = new ArrayList<String>();
        calculate(lhs,ls);
        calculate(rhs,rs);
        conv_sign(rhs);
        //Combine arrays next line. forgot how
        int left = lhs.size();
        int right = rhs.size();
        String[] fin = new String[left + right];
        System.out.println(fin);
        int poly_deg = sort_deg(deg0,deg1,deg2,fin);
        String a1,b1,c1 = "";
        a1 = reduce(deg2);
        b1 = reduce(deg1);
        c1 = reduce(deg0);
        if (poly_deg == 2)
            System.out.println("Reduced form: "+a1+" + "+b1+" + "+c1+" = 0");
        else if(poly_deg == 1)
            System.out.println("Reduced form: "+b1+" + "+c1+" = 0");
        System.out.println("Polynomial degree: " + poly_deg);
        float a = 0;
        float b = 0;
        float c = 0;
        if(poly_deg > 2)
        {
            System.out.println("The polynomial degree is stricly greater than 2, I can't solve.");
            System.exit(1);
        }
        // float discriminant = ( b*b - (Float.parseFloat("4")*(a*c)));
        discriminant = b * b - (4 * a * c);
        if (poly_deg == 0)
        {
            String s = (discriminant == 0) ? "This equation accepts all real numbers as solution.":"This equation has no solution.";
            System.out.println(s);
            System.exit(1);
        }
        if (poly_deg == 2)
        {
            if (discriminant > 0)
                System.out.println("Discriminant is strictly positive, the two solutions are:");
            else if (discriminant < 0)
                System.out.println("Discriminant is strictly negative, the two solutions are:");
            else
            {
                System.out.println("Discriminant is zero, the solution is:");
                float sol = (-b - sqrt(discriminant)) / (Float.parseFloat("2") * a);
                System.out.println(sol);
            }
            float sol1 = (-b - sqrt(discriminant)) / (Float.parseFloat("2") * a);
            float sol2 = (-b + sqrt(discriminant)) / (Float.parseFloat("2") * a);
            System.out.println(sol1);
            System.out.println(sol2);
        }
        else if (poly_deg == 1)
        {
            float sol = c/b;
            System.out.println(sol);
        }
    }
    public static void calculate(List<String> poly1,String []poly2)
    {
        int i = 0;
        int i2 = 1;
        // poly1[i] = poly2[0];
        poly1.add(poly2[0]);
    while(i2 < poly2.length)
    {
        if(poly2[i2] == "+" || poly2[i2] == "-")
        {
            i += 1;
            // poly1[i] = poly2[i2];
            poly1.add(poly2[i2]);
        }
        else
        {
            // if (poly1[i].contains("/"))
            if(poly1.get(i).contains("/"))
            {
                // String div[] = poly1[i].split("/");
                String[] div = poly1.get(i).split("/");
                if(Double.parseDouble(div[1]) == 0)
                    System.out.println(poly1.get(i) + " : Denominator is 0, Number is undefined");
                int number = Integer.parseInt(div[0]) / Integer.parseInt(div[1]);
                // poly1[i] = Integer.toString(number);
                poly1.add(Integer.toString(number));
            }
            // poly1[i] = poly1[i] + poly2[i2];
            // poly1.add(poly1.get(i)) + poly1.add( poly2[i2]);
            poly1.get(i);
            poly1.add(poly2[i2]);
        }
        i2 += 1;
    }    }
    public static void conv_sign(List<String> rhs) {
        int i = 0;
        while (i < rhs.size()) {
            if (rhs.get(i) ==  "-")
                // rhs[i] = "+" + rhs[i];
                rhs.add("+");
            else if (rhs.get(i) == "+")
                // rhs[i] = "-" + rhs[i];
                rhs.add("-");
            else
                // rhs[i] = "-" + rhs[i];
                rhs.get(i);
            i += 1;
        }
    }
    public static int sort_deg(List<String> deg0, List<String> deg1, List<String> deg2, String []fin)
    {
    int i = 0;
    int poly_deg = 0;
    while (i < fin.length)
    {
        String[] d = fin[i].split("^");
        if (d[1] == "0")
            deg0.add(fin[i]);
        else if (d[1] == "1")
            deg1.add(fin[i]);
        else if (d[1] == "2")
            deg2.add(fin[i]);
        else if (Integer.parseInt(d[1]) < 0)
            System.out.println("Cant have negative exponents");
        else if (d[1].contains("/"))
            System.out.println("Cant have fractional exponent");
        if(Integer.parseInt(d[1]) > poly_deg)
            poly_deg = Integer.parseInt(d[1]);
        i += 1;
    }
    if(deg0.size() == 0)
        deg0.add("0*X^0");
    else if(deg1.size() == 0)
        deg1.add("0*X^1");
    else if(deg2.size() == 0)
        deg2.add("0*X^2");
    return poly_deg;
}
public static String reduce(List<String> deg)
{
    int i = 0;
    float tot = 0;
    String a = "";
    String s[] = new String[deg.size()];
    if (deg.size() > 0)
    {
        String []m = deg.get(i).split("*");
        while(i < deg.size())
        {
            s = deg.get(i).split("*");
            tot = tot + Float.parseFloat(s[0]);
            i += 1;
        }
        String t[]= Float.toString(tot).split(".");
        tot = (t[1] == "0") ? Float.parseFloat(t[0]) : tot;
        a = Float.toString(tot) + "*" + m[1];
    }
    return a;
}
public static float sqrt(float number)
{
    float error = 1/100000;
    float s = number;
    while ((s-number/s) > error)
        s = (s + number / s)/2;
    return s;
}
}

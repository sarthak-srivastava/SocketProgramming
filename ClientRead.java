import java.net.*;
import java.io.*;

public class ClientRead
{
    //initialize socket and input and output stream
    private Socket socket = null;
    private DataInputStream in = null;
    private DataOutputStream out = null;

    //constructor to out ip address and port number
    public ClientRead(String address, int port)
    {
        //establish a connection
        try
        {
            socket = new Socket(address,port);
            System.out.println("Connected to "+address);

            // Take input from the terminal
            in = new DataInputStream(System.in);

            //send output to the socket
            out  = new DataOutputStream(System.out);
        }
        catch (UnknownHostException u)
        {
            System.out.println(u);
        }
        catch (IOException i)
        {
         System.out.println(i);   
        }
        //String to read input from the terminal
        String line = "";
        while(!line.equals("over"))
        {
            try
            {
                line = in.readLine();
                out.writeUTF(line);

            }
            catch(IOException i)
            {
                System.out.println(i);
            }
        }
        //close the connection

        try{
            in.close();
            out.close();
            socket.close();
        }    
        catch(IOException i)
        {
            System.out.println(i);
        }
    }
    public static void main(String[] args)
    {
            ClientRead client = new ClientRead("127.0.0.1",5000);
    }
}
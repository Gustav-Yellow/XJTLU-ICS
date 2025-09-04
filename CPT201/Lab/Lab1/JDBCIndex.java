package Lab1;/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author weiwang
 */
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class JDBCIndex{

    static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
    //replace the following three parameter values with your own ones
    static final String DB_URL = "jdbc:mysql://10.7.1.127/junhaohuang2202";
    static final String USER = "JunhaoHuang2202";
    static final String PASS = "123";

    public static void main(String[] args) {
        Connection conn;
        Statement stmt;
        ResultSet rs;
        String sql;
        String first;
        long begin;
        long end;

        try {
            Class.forName(JDBC_DRIVER);

            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            if (!conn.isClosed()) {
                System.out.println("Succeeded connecting to the Database.");
            }

            stmt = conn.createStatement();
//TEST QUERY WITHOUT AN INDEX
            //drop the existing index
            sql = "Drop INDEX numIndex ON Orf_Motif";
            stmt.execute(sql);
            System.out.println("Existing index on num dropped.");

            //prepare query without an index
            System.out.println("Start Query without an index.");
            sql = "SELECT * FROM Orf_Motif WHERE num=7";
            begin = System.currentTimeMillis();
            rs = stmt.executeQuery(sql);
            end = System.currentTimeMillis();
            System.out.println("-----------------");
            System.out.println("the result is:");
            System.out.println("-----------------");
            System.out.println(" first col" + "\t" + " second col");
            System.out.println("-----------------");

            //print actual data from the query
            while (rs.next()) {
                first = rs.getString("orf");
                System.out.println(rs.getString("acc_num") + "\t" + first);
            }
            System.out.println("End query without an index.");
            System.out.println("Query without an index takes " + (end - begin) + "milliseconds");
//END TEST QUERY WITHOUT AN INDEX

//TEST QUERY WITH AN INDEX
            //prepare query with an index
            //build an index on num for Orf_Motif
            System.out.println("Start creating an index on num.");
            sql = "CREATE INDEX numIndex ON Orf_Motif (num)";
            stmt.execute(sql);
            //index created
            System.out.println("Index on num created.");
            //start query            
            sql = "SELECT * FROM Orf_Motif WHERE num=7";
            begin = System.currentTimeMillis();
            rs = stmt.executeQuery(sql);
            end = System.currentTimeMillis();
            System.out.println("-----------------");
            System.out.println("the result is:");
            System.out.println("-----------------");
            System.out.println(" first col" + "\t" + " second col");
            System.out.println("-----------------");

            //print actual data from the query
            while (rs.next()) {
                //从列名为orf的列中读取数据
                first = rs.getString("orf");
                System.out.println(rs.getString("acc_num") + "\t" + first);
            }
            System.out.println("End query with an index.");
            System.out.println("Query with an index takes " + (end - begin) + "milliseconds");
//END TEST QUERY WITH AN INDEX

            //close database connections.
            rs.close();
            conn.close();

        } catch (ClassNotFoundException e) {

            System.out.println("Cannot find JDBC Driver!");
            e.printStackTrace();

        } catch (SQLException e) {

            e.printStackTrace();

        } catch (Exception e) {

            e.printStackTrace();

        }
    }

}

# Lab 1 JDBC

<img src="./signature/1.jpg" style="zoom:35%;" />

<img src="./Lab1/pictures/Lab1_1.png" style="zoom: 20%;" />

<img src="./Lab1/pictures/Lab1_2.png" style="zoom:20%;" />

<img src="./Lab1/pictures/Lab1_3.png" style="zoom:20%;" />

<img src="./Lab1/pictures/Lab1_4.png" style="zoom:20%;" />



# Lab2 JTA

<img src="./signature/2.jpg" style="zoom:33%;" />

<img src="./Lab2/pictures/Lab2_account1_before.png" style="zoom:20%;" />

<img src="./Lab2/pictures/Lab2_account1_after.png" style="zoom:20%;" />

<img src="./Lab2/pictures/Lab2_account2_before.png" style="zoom:20%;" />

<img src="./Lab2/pictures/Lab2_account2_after.png" style="zoom:20%;" />

<img src="./Lab2/pictures/Lab2_Database_transaction.png" style="zoom:25%;" />

# Lab 3 XML Processing

<img src="./signature/3.jpg" style="zoom:33%;" />

### DOM

<img src="./Lab3/pictures/Lab3_DOMP_result.png" style="zoom:25%;" />

### SAX

<img src="./Lab3/pictures/Lab3_SAXP_result.png" style="zoom:25%;" />



# Lab 4 KnowledgeGraph

<img src="./signature/4.jpg" style="zoom:33%;" />

### Task 1

<img src="./Lab4/pictures/Lab4_Query1.png" style="zoom:20%;" />

<img src="./Lab4/pictures/Lab4_Query2.png" style="zoom:20%;" />

<img src="./Lab4/pictures/Lab4_Query3.png" style="zoom:20%;" />

<img src="./Lab4/pictures/Lab4_Query4.png" style="zoom:20%;" />

<img src="./Lab4/pictures/Lab4_Query5.png" style="zoom:20%;" />

<img src="./Lab4/pictures/Lab4_Query6.png" style="zoom:20%;" />

<img src="./Lab4/pictures/Lab4_Query7.png" style="zoom:20%;" />

### Task 2

<img src="./Lab4/pictures/Lab4_structure.png" style="zoom:33%;" />

The RDF code of the graph:

```xml
<?xml version="1.0"?>
<rdf:RDF xmlns="urn:webprotege:ontology:0043199f-c609-4775-9f0a-efbb33303640#"
     xml:base="urn:webprotege:ontology:0043199f-c609-4775-9f0a-efbb33303640"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:webprotege="http://webprotege.stanford.edu/">
    <owl:Ontology rdf:about="urn:webprotege:ontology:0043199f-c609-4775-9f0a-efbb33303640"/>
    


    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Object Properties
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->

    


    <!-- http://webprotege.stanford.edu/R9PoKwuK24PwAYyqbtMFIXu -->

    <owl:ObjectProperty rdf:about="http://webprotege.stanford.edu/R9PoKwuK24PwAYyqbtMFIXu">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:label>workAt</rdfs:label>
    </owl:ObjectProperty>
    


    <!-- http://webprotege.stanford.edu/RBKKlJzgB7nwMXJr8uXqvII -->

    <owl:ObjectProperty rdf:about="http://webprotege.stanford.edu/RBKKlJzgB7nwMXJr8uXqvII">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:label>belongsTo</rdfs:label>
    </owl:ObjectProperty>
    


    <!-- http://webprotege.stanford.edu/RCL5CAkBFBKX0CW88JcRXHH -->

    <owl:ObjectProperty rdf:about="http://webprotege.stanford.edu/RCL5CAkBFBKX0CW88JcRXHH">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:label>studentOf</rdfs:label>
    </owl:ObjectProperty>
    


    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Classes
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->

    


    <!-- http://webprotege.stanford.edu/R9S46fKTuMhMBwY0WLnROQA -->

    <owl:Class rdf:about="http://webprotege.stanford.edu/R9S46fKTuMhMBwY0WLnROQA">
        <rdfs:subClassOf rdf:resource="http://webprotege.stanford.edu/RCbv9PMZpvT7R0q3nuG32iy"/>
        <rdfs:label>Students</rdfs:label>
    </owl:Class>
    


    <!-- http://webprotege.stanford.edu/RCbv9PMZpvT7R0q3nuG32iy -->

    <owl:Class rdf:about="http://webprotege.stanford.edu/RCbv9PMZpvT7R0q3nuG32iy">
        <rdfs:label>University</rdfs:label>
    </owl:Class>
    


    <!-- http://webprotege.stanford.edu/RDNNFK313i7wkhoJFKj3rFR -->

    <owl:Class rdf:about="http://webprotege.stanford.edu/RDNNFK313i7wkhoJFKj3rFR">
        <rdfs:subClassOf rdf:resource="http://webprotege.stanford.edu/RhY1iQdak4T9rvRARJe5an"/>
        <rdfs:label>Departments</rdfs:label>
    </owl:Class>
    


    <!-- http://webprotege.stanford.edu/RhY1iQdak4T9rvRARJe5an -->

    <owl:Class rdf:about="http://webprotege.stanford.edu/RhY1iQdak4T9rvRARJe5an">
        <rdfs:subClassOf rdf:resource="http://webprotege.stanford.edu/RCbv9PMZpvT7R0q3nuG32iy"/>
        <rdfs:label>Schools</rdfs:label>
    </owl:Class>
    


    <!-- http://webprotege.stanford.edu/RrhWazT2CcY7ClJ611CHQh -->

    <owl:Class rdf:about="http://webprotege.stanford.edu/RrhWazT2CcY7ClJ611CHQh">
        <rdfs:subClassOf rdf:resource="http://webprotege.stanford.edu/RCbv9PMZpvT7R0q3nuG32iy"/>
        <rdfs:label>Professors</rdfs:label>
    </owl:Class>
    


    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Individuals
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->

    


    <!-- http://webprotege.stanford.edu/R88U3jjQfVkgofoVEef261U -->

    <owl:NamedIndividual rdf:about="http://webprotege.stanford.edu/R88U3jjQfVkgofoVEef261U">
        <rdf:type rdf:resource="http://webprotege.stanford.edu/RDNNFK313i7wkhoJFKj3rFR"/>
        <webprotege:RBKKlJzgB7nwMXJr8uXqvII rdf:resource="http://webprotege.stanford.edu/R9a1823UiUZO0BjfikJJHPE"/>
        <rdfs:label>ICS</rdfs:label>
    </owl:NamedIndividual>
    


    <!-- http://webprotege.stanford.edu/R9a1823UiUZO0BjfikJJHPE -->

    <owl:NamedIndividual rdf:about="http://webprotege.stanford.edu/R9a1823UiUZO0BjfikJJHPE">
        <rdf:type rdf:resource="http://webprotege.stanford.edu/RhY1iQdak4T9rvRARJe5an"/>
        <webprotege:RBKKlJzgB7nwMXJr8uXqvII rdf:resource="http://webprotege.stanford.edu/RDdkcUe6hWpzcyWJCXgufjX"/>
        <rdfs:label>SAT</rdfs:label>
    </owl:NamedIndividual>
    


    <!-- http://webprotege.stanford.edu/RBBDvwUUedRODwdOMy43uz4 -->

    <owl:NamedIndividual rdf:about="http://webprotege.stanford.edu/RBBDvwUUedRODwdOMy43uz4">
        <rdf:type rdf:resource="http://webprotege.stanford.edu/RrhWazT2CcY7ClJ611CHQh"/>
        <webprotege:R9PoKwuK24PwAYyqbtMFIXu rdf:resource="http://webprotege.stanford.edu/R88U3jjQfVkgofoVEef261U"/>
        <webprotege:RBKKlJzgB7nwMXJr8uXqvII rdf:resource="http://webprotege.stanford.edu/R9a1823UiUZO0BjfikJJHPE"/>
        <rdfs:label>Mr_Wang</rdfs:label>
    </owl:NamedIndividual>
    


    <!-- http://webprotege.stanford.edu/RDdkcUe6hWpzcyWJCXgufjX -->

    <owl:NamedIndividual rdf:about="http://webprotege.stanford.edu/RDdkcUe6hWpzcyWJCXgufjX">
        <rdf:type rdf:resource="http://webprotege.stanford.edu/RCbv9PMZpvT7R0q3nuG32iy"/>
        <rdfs:label>XJTLU</rdfs:label>
    </owl:NamedIndividual>
    


    <!-- http://webprotege.stanford.edu/REGNMENmTcCbocir7TVyL6 -->

    <owl:NamedIndividual rdf:about="http://webprotege.stanford.edu/REGNMENmTcCbocir7TVyL6">
        <rdf:type rdf:resource="http://webprotege.stanford.edu/R9S46fKTuMhMBwY0WLnROQA"/>
        <webprotege:RCL5CAkBFBKX0CW88JcRXHH rdf:resource="http://webprotege.stanford.edu/R88U3jjQfVkgofoVEef261U"/>
        <webprotege:RCL5CAkBFBKX0CW88JcRXHH rdf:resource="http://webprotege.stanford.edu/RBBDvwUUedRODwdOMy43uz4"/>
        <rdfs:label>Junhao_Huang</rdfs:label>
    </owl:NamedIndividual>
</rdf:RDF>



<!-- Generated by the OWL API (version 4.5.13) https://github.com/owlcs/owlapi -->
```



# Lab 5 Java and MongoDB

<img src="./signature/5.jpg" style="zoom:33%;" />

<img src="./Lab5/pictures/Lab5_Task1.png" style="zoom:20%;" />

<img src="./Lab5/pictures/Lab5_Task2.png" style="zoom:20%;" />

<img src="./Lab5/pictures/Lab5_Task3.png" style="zoom:20%;" />



# Lab 6 XML and MongoDB

<img src="./Lab6/pictures/Lab6.png" style="zoom: 25%;" />

<img src="./Lab6/pictures/Lab6-2.png" style="zoom: 25%;" />

The Code of the In Class Test:

The code can successfully get the result below

```java
package Lab6;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.File;
import java.sql.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.LinkedHashMap;
public class LabSix {
    // initiate database information
    static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
    //replace the following three parameter values with your own ones
    static final String DB_URL = "jdbc:mysql://10.7.1.127/junhaohuang2202";
    static final String USER = "JunhaoHuang2202";
    static final String PASS = "123";
    public ArrayList<LinkedHashMap<String, Object>> extractInfo(String filepath)
    {
        ArrayList<LinkedHashMap<String, Object>> list = new ArrayList<>();
        try {
            File inputFile = new File("src/Lab6/books.xml");
            DocumentBuilderFactory dbFactory =
                    DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(inputFile);
            doc.getDocumentElement().normalize();
            System.out.println("Root element :" +
                    doc.getDocumentElement().getNodeName());
            NodeList nList = doc.getElementsByTagName("book");
            // get each book info
            for (int temp = 0; temp < nList.getLength(); temp++) {
                LinkedHashMap<String, Object> entity = new LinkedHashMap<>();
                Node nNode = nList.item(temp);
                // print book
                // System.out.println("\nCurrent Element:" + nNode.getNodeName() 
                + temp);
                if (nNode.getNodeType() == Node.ELEMENT_NODE) {
                    Element eElement = (Element) nNode;
                    // get book_id
                    String book_id = eElement.getAttribute("id");
                    // get author
                    String author =
                            eElement.getElementsByTagName("author").item(0).getTextContent();
                    // get title
                    String title =
                            eElement.getElementsByTagName("title").item(0).getTextContent();
                    // get genre
                    String genre =
                            eElement.getElementsByTagName("genre").item(0).getTextContent();
                    // get price
                    String price =
                            eElement.getElementsByTagName("price").item(0).getTextContent();
                    // get date
                    String date =
                            eElement.getElementsByTagName("publish_date").item(0).getTextContent();
                    // get description
                    String description =
                            eElement.getElementsByTagName("description").item(0).getTextContent();
                    // add to map
                    entity.put("book_id", book_id);
                    entity.put("author", author);
                    entity.put("title", title);
                    entity.put("genre", genre);
                    entity.put("price", price);
                    entity.put("date", date);
                    entity.put("description", description);
                    // 讲当前的 entity 添加到 arraylist 当中
                    list.add(entity);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return list;
    }
    public void databaseOperation(ArrayList<LinkedHashMap<String, Object>>
                                          list){
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
            //prepare query without an index
            System.out.println("Start to insert values into the database");
            for (int i = 0; i < list.size(); i++) {
                LinkedHashMap<String, Object> entity = list.get(i);
                try {
                    String priceStr = (String) entity.get("price");
                    String dateStr = (String) entity.get("date");
                    String bookId = (String) entity.get("book_id");
                    String author = (String) entity.get("author");
                    String title = (String) entity.get("title");
                    String genre = (String) entity.get("genre");
                    String description = (String) entity.get("description");
                    // check null value
                    if (priceStr == null || dateStr == null || bookId == null ||
                            author == null || title == null || genre == null || description == null) {
                        System.out.println("Skipping incomplete data: " +
                                entity);
                        continue;
                    }
                    // convert float and date
                    float price = Float.parseFloat(priceStr);
                    DateTimeFormatter formatter =
                            DateTimeFormatter.ofPattern("yyyy-MM-dd");
                    LocalDate localDate = LocalDate.parse(dateStr, formatter);
                    java.sql.Date sqlDate = java.sql.Date.valueOf(localDate);
                    // 构建 SQL
                    sql = "INSERT INTO books (book_id, author, title, genre, 
                    price, publish_date, description) VALUES (?, ?, ?, ?, ?, ?, ?)";
                    try (PreparedStatement pstmt = conn.prepareStatement(sql))
                    {
                        pstmt.setString(1, bookId);
                        pstmt.setString(2, author);
                        pstmt.setString(3, title);
                        pstmt.setString(4, genre);
                        pstmt.setFloat(5, price);
                        pstmt.setDate(6, sqlDate);
                        pstmt.setString(7, description);
                        int affectedRows = pstmt.executeUpdate();
                        System.out.println("Rows affected: " + affectedRows);
                    }
                } catch (SQLException e) {
                    System.err.println("SQL error: " + e.getMessage());
                    e.printStackTrace();
                } catch (Exception e) {
                    System.err.println("Error: " + e.getMessage());
                    e.printStackTrace();
                }
            }
            System.out.println("End query.");
            conn.close();
            //close database connections.
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
    public static void main(String[] args) {
        LabSix labSix = new LabSix();
        ArrayList<LinkedHashMap<String, Object>> result =
                labSix.extractInfo("books.xml");
        for (LinkedHashMap<String, Object> entity : result) {
            System.out.printf((String) entity.get("book_id"));
        }
        labSix.databaseOperation(result);
    }
}
```




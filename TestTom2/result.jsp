<%@ page import="java.util.*"%>

<html>
  <body>
    <h1 align="center">Beer Recommendation JSP </h1>
      <p>

        <% 
          List styles = (List)request.getAttribute("styles");
          Iterator it = styles.iterator();
          while (it.hasNext()){
  	        out.print("<br>TRY: "+ it.next());
          }
        %>

      </p>
  </body>
</html>
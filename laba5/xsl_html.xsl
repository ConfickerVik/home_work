<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<html>
		<body>
		<h2>Tariffs</h2>
		<table border="1">
			<tr bgcolor="#9acd32">
				<th>Name</th>
				<th>OperatorName</th>
				<th>Payroll</th>
				<th>Inside</th>
				<th>Outside</th>
				<th>Stationary</th>
				<th>SMSPrice</th>
				<th>FavoriteNumber</th>
				<th>Tariffication</th>
				<th>TarrifConnectionFee</th>
			</tr>
			<xsl:for-each select="Tariffs/Name">
     		 	<tr>
       				<td><xsl:value-of select="@name"/></td>
       				<td><xsl:value-of select="OperatorName"/></td>
       				<td><xsl:value-of select="Payroll"/></td>
					<td><xsl:value-of select="CallPrices/Inside"/></td>
       				<td><xsl:value-of select="CallPrices/Outside"/></td>
					<td><xsl:value-of select="CallPrices/Stationary"/></td>
					<td><xsl:value-of select="SMSPrice"/></td>
					<td><xsl:value-of select="Parametrs/FavoriteNumber"/></td>
       				<td><xsl:value-of select="Parametrs/Tariffication"/></td>
					<td><xsl:value-of select="Parametrs/TarrifConnectionFee"/></td>
      			</tr>
      			</xsl:for-each>
   		 </table>
 	 </body>
  	</html>
</xsl:template>
</xsl:stylesheet>

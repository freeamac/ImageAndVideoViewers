<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/TR/REC-html40">
  <xsl:output method="html" indent="yes"/>
  <xsl:template match="/slideshow">
    <HTML>
    <HEAD>
    <META http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
    <TITLE><xsl:value-of select="title"/></TITLE>
    </HEAD>
    <BODY>
    <H1><xsl:value-of select="title"/></H1>
    <xsl:for-each select="picture">
      <HR/>
      <TABLE WIDTH="100%">
        <TR>
	  <TD ALIGN="CENTER">
            <xsl:element name="img">
	      <xsl:attribute name="height">576</xsl:attribute>
	      <xsl:attribute name="width">768</xsl:attribute>
              <xsl:attribute name="src">
                <xsl:value-of select='image'/>
              </xsl:attribute>
            </xsl:element>
	  </TD>
	</TR>
	<TR>
	  <TD ALIGN="CENTER">
            <B>
              <xsl:value-of select="caption"/>
            </B>
	  </TD>
	</TR>
	<TR>
	    <TD ALIGN="LEFT">
	    Location: <xsl:value-of select="location"/>
	    <BR/>
	    Date: <xsl:value-of select="date"/>
	    </TD>
	</TR>
	<TR>
	    <TD ALIGN="LEFT">
	    ASA: <xsl:value-of select="asa"/>
	    <BR/>
	    Roll Number: <xsl:value-of select="roll_num"/>
	    <BR/>
	    Roll Max: <xsl:value-of select="roll_max"/>
	    </TD>
	</TR>
      </TABLE>
    </xsl:for-each>
    <HR/>
    <xsl:value-of select="copyright"/>
    </BODY>
    </HTML>
  </xsl:template>
</xsl:stylesheet>

function printData()
{
   var divToPrint=document.getElementById("tableauImpression");
   var htmlToPrint = '' +
        '<style type="text/css">' +
        'table td, table td {' +
        'border:1px solid black;' +
        'padding;0.5em;' +
        '}' +
        'table {' +
        'border-collapse: collapse;'+
        '}' +
        '</style>';

    htmlToPrint += divToPrint.outerHTML;
   newWin= window.open("");
   newWin.document.write(htmlToPrint);
   newWin.print();
   newWin.close();
}
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

$(function(){
    $(".sous-menu").hide();
    var ouvert = false;

    $(".btnDer").on("click",function(){
        if(ouvert){
            $(this).children("ul").slideUp(300);
            ouvert = false;
        }else{
            $(this).children("ul").slideDown(300);
            ouvert = true;
        }
    });


    $('.cb-value').on("click",function() {
        console.log("bjr")
        var mainParent = $(this).parent('.toggle-btn');
        $.get("/onAdmin");
        if($(mainParent).hasClass('active')) {
            $(mainParent).removeClass('active');
        } else {
            $(mainParent).addClass('active');
        };
    })
});

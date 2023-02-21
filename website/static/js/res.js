$(document).ready(function(){
    $(".chat_on").click(function(){
        $(".Layout").toggle();
        $(".chat_on").hide(300);
    });
    
       $(".chat_close_icon").click(function(){
        $(".Layout").hide();
           $(".chat_on").show(300);
    });
    
});

$(document).ready(function(){
    $("#send_button").click(function(e){
        e.preventDefault();
        var input = $('#input').val();
        $.ajax({
            url : "/chat",   //change url
            type: "post",
            mode: 'no-cors',
            crossdomain: true,
            withCredentials: false,
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json;charset=UTF-8',
                "Access-Control-Allow-Origin": "*"
            },
            data: JSON.stringify({data:input}),
            success: function(response){
                $('.customer').append(`<p>${input}</p>`)
                window.location.href= ('/category/sports')
            }
        });

    });

});

// $(function(){
    
//     // Configure/customize these variables.
//     var showChar = 100;  // How many characters are shown by default
//     var ellipsestext = "...";
//     var moretext = "Show more >";
//     var lesstext = "Show less";
//     var readsummary = 'read summary'
    
//     $('.more').each(function() {
        
//         var content = $(this).html();
//         if(content.length > showChar) {
 
//             var c = content.substr(0, showChar);
//             var h = content.substr(showChar, content.length - showChar);
 
//             var html = c + '<span class="moreellipses">' + ellipsestext+ '&nbsp;</span><span class="morecontent"><span>' + h + '</span>&nbsp;&nbsp;<a href="" class="morelink">' + moretext + '</a>&nbsp;&nbsp;</span>';
 
//             $(this).html(html);
          
//         }
        
//     });
 
//     $(".morelink").click(function(){
//         if($(this).hasClass("less")) {
//             $(this).removeClass("less");
//             $(this).html(lesstext);
//         } else {
//             $(this).addClass("less");
//             $(this).html(moretext);
//         }
//         $(this).parent().prev().toggle();
//         $(this).prev().toggle();
//         return false;
//     });
   
// });
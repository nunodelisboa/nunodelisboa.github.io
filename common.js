(function(){
    $('fieldset').hover(
        function(){ 
            var $field = $(this);
            $field.css('border-color','blueviolet');
            $field.find('legend').css('color','blueviolet');
        },
        function(){
            var $field = $(this);
            $field.css('border-color', '');
            $field.find('legend').css('color','');
        }          
     );

})()

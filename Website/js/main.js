// animate smooth scrolling
$('#View-Work').on('click', function() {
    const Codes = $('#Codes').position().top;
    
    $('html, body').animate(
        {
            scrollTop: Codes

        },
        900
    );
  });

  
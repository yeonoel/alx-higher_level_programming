$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (event) {
      if (event.keycode === 13) {
        translate();
      }
    });
  });

  function translate () {
    const lang = $('INPUT#language_code').val();
    $.get(`https://stefanbohacek.com/hellosalut/?lang=${lang}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
});

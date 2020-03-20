window.onload = function () {

  const getId = (url) => {
      const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
      const match = url.match(regExp);

      return (match && match[2].length === 11) ? match[2] : null;
  };

  $('iframe').each(function() {

    const videoUrl = $(this).attr('src');
    const videoId = getId(videoUrl);
    $(this).attr('src', `//www.youtube.com/embed/${videoId}`);
  });
}
function redirectToPage(url) 
{
    document.body.style.opacity = 0;
    setTimeout(function () 
    {
        window.location.href = url;
    }, 500);
}
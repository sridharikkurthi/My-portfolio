document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    console.log(`Contact request from ${name} (${email}): ${message}`);

    document.getElementById('contact-form').reset();

    alert('Thank you for contacting us! Your message has been sent.');

    notifyAdmin(name, email, message);
});

function notifyAdmin(name, email, message) {
    console.log(`Admin notified: ${name} (${email}) sent a message.`);
}

document.getElementById('more-about-me').addEventListener('click', function() {
    const aboutSection = document.getElementById('about');
    aboutSection.scrollIntoView({ behavior: 'smooth' });
    alert("More details about Ikkurthi Gangasridhar are available below.");
});
var typed = new Typed(".t", {
    strings: ["Frontend Designer", "Python Fullstack Developer."],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
});
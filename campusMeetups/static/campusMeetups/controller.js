
document.addEventListener('DOMContentLoaded', function () {

    // Use buttons to toggle between views

    document.querySelector('#createMeetup').addEventListener('click', createMeetup);
    document.querySelector('#profile').addEventListener('click', showProfile);
    document.querySelector('#activePosts').addEventListener('click', allMeetups);
    document.querySelector('#map').addEventListener('click', showMap);
    document.querySelector('#enrolled').addEventListener('click', enrolled);

});



function createMeetup() {
    const create = document.querySelector('#create_view')
    create.style.display = 'block';
    document.querySelector('#meetups_view').style.display = 'none';
    document.querySelector('#profile_view').style.display = 'none';
    document.querySelector('#show_map').style.display = 'none';
    document.querySelector('#enrolled_view').style.display = 'none';

}

function showProfile() {
    const profileView = document.querySelector('#profile_view');
    document.querySelector('#profile_view').style.display = 'block';
    document.querySelector('#create_view').style.display = 'none';
    document.querySelector('#meetups_view').style.display = 'none';
    document.querySelector('#show_map').style.display = 'none';
    document.querySelector('#enrolled_view').style.display = 'none';
    //call function to make heading and clear view on inital load (string, parent)
    headingClearPage('<h1>My Profile</h1>', profileView)
    fetch("/profile").then(response => response.json()).then(data =>
        data.forEach((user) => {
            console.log(user);
            const profileData = document.createElement("div");
            profileData.innerHTML = `<div class="card meetupCard" style="width: 50rem;">
                                    <div class="card-body">
                                    <h4 class="card-title">Name: ${user.first_name}${user.last_name}</h4>
                                    <h6>Email: ${user.email}</h6>
                                    <p class="card-text">Major</p>
                                    <h6>Some other user data</h6>
                                    <h6>More data for the user</h6>
                                    </div>
                                    </div>`;
            profileView.append(profileData);
        }));

}

function allMeetups() {
    const activePosts = document.querySelector('#meetups_view');
    document.querySelector('#meetups_view').style.display = 'block';
    document.querySelector('#profile_view').style.display = 'none';
    document.querySelector('#create_view').style.display = 'none';
    document.querySelector('#show_map').style.display = 'none';
    document.querySelector('#enrolled_view').style.display = 'none';
     //call function to make heading and clear view on inital load (string, parent)
    headingClearPage('<h1>Active Posts</h1>', activePosts)
    fetch("/meetups").then(response => response.json()).then(data =>
        data.forEach((meetup) => {
            console.log(meetup);
            const signUpLink = document.querySelector('#signUplink').value
            const showMeetup = document.createElement("div");
            showMeetup.innerHTML = `<div class="card meetupCard" style="width: 50rem;">
                                    <div class="card-body">
                                    <h4 class="card-title">${meetup.subjType}</h4>
                                    <h6>Course: ${meetup.subjCode}</h6>
                                    <p class="card-text">Description: ${meetup.description}</p>
                                    <h6>Building: ${meetup.buildingNames}</h6>
                                    <h6>Room: ${meetup.meetupRoom}</h6>
                                    <form id="signUp" method="post" action="${signUpLink}">
                                    <input type="hidden" name="meetupID" value="${meetup.id}" />
                                    <input type="submit" class="btn btn-primary" value="Sign Up!" />
                                    </form>
                                    </div>
                                    </div>`;

            activePosts.append(showMeetup);
        }));

}

function enrolled() {
    const enrolledView = document.querySelector('#enrolled_view')
    enrolledView.style.display = 'block';
    document.querySelector('#profile_view').style.display = 'none';
    document.querySelector('#create_view').style.display = 'none';
    document.querySelector('#meetups_view').style.display = 'none';
    document.querySelector('#show_map').style.display = 'none';
    //call function to make heading and clear view on inital load (string, parent) 
    headingClearPage('<h1>Enrolled Meetups</h1>', enrolledView)
    fetch("/enrolled").then(response => response.json()).then(data =>
        data.forEach((enroll) => {
            console.log(enroll);
            const showEnrolledMeetup = document.createElement("div");
            showEnrolledMeetup.innerHTML = `<div class="card meetupCard" style="width: 50rem;">
                                    <div class="card-body">
                                    <h4 class="card-title">${enroll.subjType}</h4>
                                    <h6>Course: ${enroll.subjCode}</h6>
                                    <p class="card-text">Description: ${enroll.description}</p>
                                    <h6>Building: ${enroll.buildingNames}</h6>
                                    <h6>Room: ${enroll.meetupRoom}</h6>
                                    </div>
                                    </div>`;
            enrolledView.append(showEnrolledMeetup);
        }))
}

function showMap() {
    const mapView = document.querySelector('#show_map');
    mapView.style.display = 'block';
    document.querySelector('#profile_view').style.display = 'none';
    document.querySelector('#create_view').style.display = 'none';
    document.querySelector('#meetups_view').style.display = 'none';
    document.querySelector('#enrolled_view').style.display = 'none';
    //call function to make heading and clear view on inital load (string, parent) 
    headingClearPage('<h1>Campus Map</h1>', mapView)
    const mapBox = document.createElement("iframe");
    Object.assign(mapBox, {
        src: 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3022.4367092569464!2d-73.42927392043208!3d40.75241867870058!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e82afe99b445e9%3A0x6c53280083cbf6be!2sFarmingdale%20State%20College!5e0!3m2!1sen!2sus!4v1596479364656!5m2!1sen!2sus',
        width: 600,
        height: 450,
        frameborder:0,
        style: 'border:0;',
        allowfullscreen:'',
        tabindex:0
    })
    mapView.append(mapBox);

    
}

function headingClearPage(headTitle, parent) {
    heading = document.createElement("h1")
    heading.innerHTML = headTitle;
    parent.innerHTML = '';
    parent.append(heading);

    //extend function to have a block and then clear other views
}



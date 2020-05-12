// TODO: Replace the following with your app's Firebase project configuration
const firebaseConfig = {
    apiKey: "AIzaSyAtl204Z-7BI3KHjlk3XtU7ivP8PaO5Jr4",
    authDomain: "dj-site-3b616.firebaseapp.com",
    databaseURL: "https://dj-site-3b616.firebaseio.com",
    projectId: "dj-site-3b616",
    storageBucket: "dj-site-3b616.appspot.com",
    messagingSenderId: "943029467573",
    appId: "1:943029467573:web:2bebfa08e08d33b89d01fc",
    measurementId: "G-QWYJZX5Z2Y"
};

const google = new firebase.auth.GoogleAuthProvider();
const facebook = new firebase.auth.FacebookAuthProvider();

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
// Expose firebase methods
var auth = firebase.auth();
var firestore = firebase.firestore();
var signInWithGoogle = (errorFn = null) => {
    auth.signInWithPopup(google).catch((error) => errorFn(error));
};
var signInWithFacebook = (errorFn = null) => {
    auth.signInWithPopup(facebook).catch((error) => errorFn(error));
};
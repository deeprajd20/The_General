const outputDiv = document.getElementById("output");

// Fetch API response
fetch("http://localhost:8000/api/chat")
    .then(res => res.text())
    .then(data => {
        outputDiv.innerHTML = data;
    });
// ----- THREE JS CUBE -----
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);

// Enable transparency
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });

// Transparent background (IMPORTANT)
renderer.setClearColor(0x000000, 0);

// Full screen
renderer.setSize(window.innerWidth, window.innerHeight);

// Add canvas on top of body
document.body.appendChild(renderer.domElement);

// Cube
const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial({
    color: 0x00ff00,
    wireframe: true
});
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

// camera.position.z = 4;
camera.position.x = 1;
camera.position.y = 1;
camera.position.z = 2;
// Animation
function animate() {
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    renderer.render(scene, camera);
}

animate();

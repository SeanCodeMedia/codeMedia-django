import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.118.3/build/three.module.js';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.121.1/examples/jsm/controls/OrbitControls.js';


var vertexShader = `
    uniform float time;
    uniform vec3 basePos;
    varying vec3 vPos;
    varying vec2 vUv;
    void main()	{
      vPos = position + basePos;
      vUv = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0);
    }
  `;
  var fragmentShader = `
    /* based on http://madebyevan.com/shaders/grid/ */
  
    //#extension GL_OES_standard_derivatives : enable

    varying vec3 vPos;
    varying vec2 vUv;
    uniform float time;
    uniform vec3 color;
    
    float line(float width, vec2 step){
      
      vec2 coord = vUv / step;
      //coord.x += sin(coord.y - time * 5.) + time; // wavy effect + "rotation"

      vec2 grid = abs(fract(coord - 0.5) - 0.5) / fwidth(coord * width);
      float line = min(grid.x, grid.y);
      
      return 1. - min(line, 1.0);
    }
    
    // from https://www.shadertoy.com/view/MsjSzc
    //Divided per 7 -> 1/7 = 0.1428571428571429
    float Maskline(float pos,float lineNumber)
    {    
      return step(pos,0.1428571428571429 * lineNumber) - (step(pos,0.1428571428571429 * (lineNumber - 1.)));
    }

    vec3 GetRainbowColor(float i)
    {
        //Step Violet
      vec3 Violet = 	vec3(0.57,0.0, 1.0) 	*  Maskline(i,7.);
      vec3 Purple = 	vec3(0.27,0.0, 0.51)	*  Maskline(i,6.);
      vec3 blue 	=	vec3(0.0, 	0.0, 1.0) 	*  Maskline(i,5.);
      vec3 Green	=	vec3(0.0, 	1.0, 0.0) 	*  Maskline(i,4.);
      vec3 Yellow =	vec3(1.0, 	1.0, 0.0) 	*  Maskline(i,3.);
      vec3 Orange =	vec3(1.0, 	0.5, 0.0) 	*  Maskline(i,2.);
      vec3 Red	=	vec3(1.0, 	0.0, 0.0) 	*  Maskline(i,1.);
      return Violet + Purple + blue + Green + Yellow + Orange + Red;
    }
    
    vec3 SmoothRainbowColor(float i)
    {
      i *= 0.1428571428571429 * 6.;
      float gradinStep = mod(i,0.1428571428571429) * 7.;    
      vec3 firstColor = GetRainbowColor(i);
      vec3 NextColor = GetRainbowColor(i + 0.1428571428571429);    
      return mix(firstColor,NextColor, gradinStep);
    }
    
    void main() {
      float v = line(1., vec2(1. / 24., 0.1));
      
      float s = 500.; // step
      float mp = mod(vPos.z - time * 100., s);
      float sm = 1. - smoothstep(0., 5., mp) * (1. - smoothstep(s - 20.,s,mp));
      
      vec3 c = mix(vec3(0.125, 0., .125), vec3(0., 1., 1.), sm); // mixing base colour of lines and colour of wave
      vec3 rainbow = SmoothRainbowColor(1. - mod(vPos.z - 275., 550.) / 550.);
      c = mix(rainbow, c, v);
      //c = mix(color, c, v);
      
      gl_FragColor = vec4(c, 1.0);
    }
  `;

// const canvas = document.querySelector('#canvas');
// const renderer = new THREE.WebGLRenderer({canvas});

// const fov = 75;
// const aspect = 2;  // the canvas default
// const near = 0.1;
// const far = 5;

// const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
// camera.position.z = 2;
// camera.position.multiplyScalar( 2 ); 

// // const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 1, 1100 );
// // camera.position.z = 0.01;

// const scene = new THREE.Scene();


// // const controls = new OrbitControls( camera, renderer.domElement );
// // controls.update();
// // controls.enableZoom = false;
// // controls.minPolarAngle = 1.5;
// // controls.maxPolarAngle = 1; 
// // controls.minAzimuthAngle = -0.08250618320397618
// // controls.maxAzimuthAngle =  0.08250618320397618
// const boxWidth = 1;
// const boxHeight = 1;
// const boxDepth = 1;
// const geometry = new THREE.BoxGeometry(boxWidth, boxHeight, boxDepth);

// //const material = new THREE.MeshBasicMaterial({color: 0x44aa88});
// const material = new THREE.MeshPhongMaterial({color: 0x44aa88}); 

// const cube = new THREE.Mesh(geometry, material);


// const radius = 0.5;  // ui: radius
// const detail = 2;  // ui: detail
// const Circlegeometry = new THREE.DodecahedronGeometry(radius, detail);
// const circle = new THREE.Mesh(Circlegeometry, material);
// circle.position.x = -2 


// // const cubes = [
// //   makeInstance(geometry, 0x44aa88,  0),
// //   makeInstance(geometry, 0x8844aa, -2),
// //   makeInstance(geometry, 0xaa8844,  2),
// // ];


// // function makeInstance(geometry, color, x) {
// //   const material = new THREE.MeshPhongMaterial({color});
 
// //   const cube = new THREE.Mesh(geometry, material);
// //   scene.add(cube);
 
// //   cube.position.x = x;
 
// //   return cube;
// // }

// let mouseX = 0, mouseY = 0;
// let windowHalfX = window.innerWidth / 2;
// let windowHalfY = window.innerHeight / 2;

// const texture = new THREE.TextureLoader().load( './static/images/bg.jpg', render );
// texture.mapping = THREE.EquirectangularReflectionMapping; // look at this
// scene.background = texture;

// const loader = new THREE.FontLoader();

// loader.load('./static/js/Oswald_Regular.json', function (font) {
//     const geometry = new THREE.TextGeometry('Sean Code Media', {
//         font: font,
//         size: 0.6,
//         height: 1,
//         curveSegments: 12,
//         bevelEnabled: false,
//         bevelOffset: 0,
//         bevelSegments: 1,
//         bevelSize: 0.3,
//         bevelThickness: 1
//     });
//     const materials = [
//         new THREE.MeshPhongMaterial({ color: 0xFFFFFF }), // front
//         new THREE.MeshPhongMaterial({ color: 0x949494}) // side
//     ];
//     const textMesh1 = new THREE.Mesh(geometry, materials);
//     //textMesh1.castShadow = true
//     textMesh1.position.y += 0
//     textMesh1.position.x -= 2.5
//     textMesh1.rotation.y = 0
//     scene.add(textMesh1)
// });


// function onDocumentMouseMove( event ) {

// 			mouseX = ( event.clientX - windowHalfX )/1000;
// 			mouseY = ( event.clientY - windowHalfY )/1000;

// 		}

// function onWindowResize() {

// 				windowHalfX = window.innerWidth / 2;
// 				windowHalfY = window.innerHeight / 2;

// 				camera.aspect = window.innerWidth / window.innerHeight;
// 				camera.updateProjectionMatrix();

// 				renderer.setSize( window.innerWidth, window.innerHeight );

// }



// function main() {
//   document.addEventListener( 'mousemove', onDocumentMouseMove );
//   window.addEventListener( 'resize', onWindowResize );
//   const color = 0xFFFFFF;
//   const intensity = 1;
//   const light = new THREE.DirectionalLight(color, intensity);
//   light.position.set(-1, 2, 4);
//   scene.add(light);

   
//   // scene.add(cube);
//   // scene.add(circle);
//   renderer.render(scene, camera);

// }


// main()


//  function resizeRendererToDisplaySize(renderer) {
//       const canvas = renderer.domElement;
//       const pixelRatio = window.devicePixelRatio;
//       const width  = canvas.clientWidth  * pixelRatio | 0;
//       const height = canvas.clientHeight * pixelRatio | 0;
//       const needResize = canvas.width !== width || canvas.height !== height;
//       if (needResize) {
//         renderer.setSize(width, height, false);
//       }
//       return needResize;
//     }


// function render(time) {
//   time *= 0.001;  // convert time to seconds

//   if (resizeRendererToDisplaySize(renderer)) {
//     const canvas = renderer.domElement;
//     camera.aspect = canvas.clientWidth / canvas.clientHeight;
//     camera.updateProjectionMatrix();
//   }


// 	//controls.update();
//   // cube.rotation.x = time*2;
//   // cube.rotation.y = time*3;
//   // circle.rotation.x = time*2;
//   // circle.rotation.y = time*2;
//   // //circle.rotation.z = time*2;
//  // console.log(controls.getAzimuthalAngle())

//     const canvas = renderer.domElement;
//   camera.aspect = canvas.clientWidth / canvas.clientHeight;
//   camera.updateProjectionMatrix();


//  // cubes.forEach((cube, ndx) => {
//  //    const speed = 1 + ndx * .1;
//  //    const rot = time * speed;
//  //    cube.rotation.x = rot;
//  //    cube.rotation.y = rot;
//  //  });

//  	 camera.position.x += ( mouseX - camera.position.x )*0.05;
// 	 camera.position.y += (  mouseY - camera.position.y ) * 0.05;
// 	 camera.lookAt( scene.position );
//     renderer.render(scene, camera);
 
//   requestAnimationFrame(render);
// }
// requestAnimationFrame(render);


// var scene = new THREE.Scene();
// var camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);
// camera.position.set(0, 0, 250);
// var renderer = new THREE.WebGLRenderer({
//   antialias: true
// });
// renderer.setSize(window.innerWidth, window.innerHeight);
// renderer.setClearColor(0x404040);
// document.body.appendChild(renderer.domElement);

// var controls = new OrbitControls(camera, renderer.domElement);

// const texture = new THREE.TextureLoader().load( './static/images/code.jpg' );

// var planes = [];
// for (let i = 0; i < 5; i++) {
//   let geometry = new THREE.CylinderBufferGeometry(50, 50, 100, 6, 1, true);

//   geometry.rotateX(-Math.PI * .5);
//   let material = new THREE.ShaderMaterial({
//     uniforms: {
//       time: {
//         value: 0
//       },
//       basePos: {
//         value: new THREE.Vector3()
//       },
//       color:{
//         value: new THREE.Color().setScalar(.5 + ((i + 1) / 5) * .5)
//       }
//     },
//     vertexShader: vertexShader,
//     fragmentShader: fragmentShader, 
//     side: THREE.DoubleSide
//   });

//   let plane = new THREE.Mesh(geometry, material);
//   plane.position.set(0, 0, 270 - i * 110);
//   scene.add(plane);
//   planes.push(plane);
// }

// var clock = new THREE.Clock();
// var time = 0;
// var delta = 0;
// var direction = new THREE.Vector3(0, 0, 1);
// var speed = 50; //units a second

// render();

// function render() {
//   requestAnimationFrame(render);
  
//   delta = clock.getDelta();
//   time += delta;
//   planes.forEach(function(plane) {
//   	plane.position.addScaledVector(direction, speed * delta);
//     if (plane.position.z > 275) plane.position.z = -275 + ((plane.position.z - 275) % 550);
//      plane.material.uniforms.time.value = time;
//      plane.material.uniforms.basePos.value.copy(plane.position);
//   });

//   renderer.render(scene, camera);
// }



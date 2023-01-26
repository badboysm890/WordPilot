<script>
	// @ts-nocheck

	import { onMount } from 'svelte';
	import Quill from 'quill';
	let quill = null;

	
	function createDocument() {

		var url = document.querySelector('.youtubeUrl').value;
		try {
			var videoId = new URL(url).searchParams.get("v");
			document.querySelector('.card-img-top').src = `https://img.youtube.com/vi/${videoId}/maxresdefault.jpg`;
		} catch (error) {
			alert('Please enter a valid youtube url');
			return false;
		}
		
		document.querySelector('.spinny').classList.remove('d-none');
		document.querySelector('.getCard').classList.add('d-none');
		let container = document.getElementById('editor');
		var myHeaders = new Headers();
		myHeaders.append('Content-Type', 'application/json');
		var requestOptions = {
			method: 'POST',
			headers: myHeaders,
			redirect: 'follow'
		};
		fetch(
			'http://127.0.0.1:5000/getData?url='+url,
			requestOptions
		)
			.then((response) => response.text())
			.then((result) => {
				let data = JSON.parse(result);
				console.log(data);
				if (data == null) {
					console.log('data is null');
					document.querySelector('.getCard').classList.remove('d-none');
					return;
				} else {
					// remove the spinny
					document.querySelector('.spinny').classList.add('d-none');
					document.querySelector('#editor').classList.remove('d-none');
				}
				for (const [key, value] of Object.entries(data)) {
					console.log(`${key}: ${value}`);
					for (const [keys, values] of Object.entries(value)) {
						console.log(`${keys}: ${values}`);
						if (keys == 'heading') {
							document.querySelector('#editor').innerHTML += `<br><h2>${values}</h2>`;
						}
						if (keys == 'text') {
							document.querySelector('#editor').innerHTML += `<p>${values}</p> <br>`;
						}
					}
				}

				quill = new Quill(container, {
					modules: {
						toolbar: [
							['bold', 'italic', 'underline', 'strike'],
							['link', 'code-block', 'image'],
							[{ list: 'ordered' }, { list: 'bullet' }],
							[{ script: 'sub' }, { script: 'super' }],
							[{ indent: '-1' }, { indent: '+1' }],
							[{ direction: 'rtl' }],
							[{ size: ['small', false, 'large', 'huge'] }],
							[{ header: [1, 2, 3, 4, 5, 6, false] }],
							[{ color: [] }, { background: [] }],
							[{ font: [] }],
							[{ align: [] }],
							['clean']
						]
					},
					placeholder: 'Type something...',
					theme: 'snow' // or 'bubble'
				});
			})
			.catch((error) => console.log('error', error));
		// loop through the object and print the key and value
	}

	onMount(() => {});
</script>

<svelte:head>
	<link
		href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
		rel="stylesheet"
		integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
		crossorigin="anonymous"
	/>
	<src
		src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
		integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
		crossorigin="anonymous"
	/>
	<!-- poppins font -->

	<link
		href="https://fonts.googleapis.com/css?family=Poppins:100,100italic,200,200italic,300,300italic,regular,italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic"
		rel="stylesheet"
	/>
	<link href="//cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet" />
	<style>
		/* card height 500px */

		.card {
			height: 100%;
		}

		/* poppins font */

		@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

		/* font family Poppins for everythong */

		* {
			font-family: 'Poppins', sans-serif;
		}
/* 
		.bg-dark {
			background-color: #28304e !important;
		} */
	</style>
</svelte:head>

<body>
	<style>
		main {
			text-align: center;
			padding: 1em;
			margin: 0 auto;
		}

		#editor {
			/* height: screen height */
			height: 90vh;
		}
		/* glossy class has a gradient background */
		.glossy {
			/*  light pink to purple */
			background: linear-gradient(90deg, #fbc2eb 0%, #a6c1ee 100%);
		}

		@media (min-width: 640px) {
			main {
				max-width: none;
			}
		}

		/* left-side-bar should hide when on mobile mode */
		@media (max-width: 640px) {
			.left-side-bar {
				display: none;
			}
		}

		.card-bgs {
			background: rgb(172, 0, 0);
			background: linear-gradient(
				90deg,
				rgba(172, 0, 0, 1) 0%,
				rgba(6, 0, 5, 1) 53%,
				rgba(225, 69, 252, 1) 100%
			);
		}
	</style>

	<nav class="navbar navbar-dark bg-dark">
		<span class="navbar-brand p-2">
			<img src="/logo.png" alt="" width="200" />
		</span>

		<button class="btn btn-outline-light m-2">Sign Up</button>
	
	</nav>

	<div>
		<!-- side bar in the left side in same colour as nav -->
		<div class="bg-dark left-side-bar" style="height: 100vh; width: 20%; float: left;">
			<div class="d-flex flex-column">
				<!-- make the card 20% overflow through the side bar to the other div -->
				<div class="my-5 card m-3">
					<!-- show an youtube thumbnail -->
					<img
						src="https://q5n8c8q9.rocketcdn.me/wp-content/uploads/2019/09/YouTube-thumbnail-size-guide-best-practices-top-examples.png.webp"
						class="card-img-top"
						alt="..."
						width="10%"
					/>
				</div>

				<!-- another card saying free for 10 days after please sign in -->
				<div class="my-2 glossy card m-3">
					<!-- <div class="card-header">Note</div> -->
					<div class="card-body">
						<h5 class="card-title">Get Extras</h5>
						<p class="card-text">
							Sign up to get extra features like generating images, audio transpiler and more.
						</p>
						<span class="btn btn-primary">Register Now</span>
					</div>
				</div>
			</div>

			<!-- create a card of youtube thumbnail -->
		</div>
		<!-- center the div inside -->
		<div class="d-flex justify-content-center">
			
			<main class="w-100">
				<div class="getCard card bg-dark text-white">
					<div class="card-body h-100">
						<h2
							class="card-title
						"
						>
							<b>Youtube</b> to <b>Blog </b> Post 📜
						</h2>
						<p class="card-text">Enter a Youtube URL. Lets make a blog post</p>

						<div class="input-group mb-3">
							<input type="text" class="form-control youtubeUrl" placeholder="Youtube URL" />
							<!-- onclick call the  createDocument function -->
							<button class="btn btn-outline-danger" type="button" id="button-addon2" on:click|once={createDocument}>
								Create
							</button>
						</div>
					</div>
				</div>
				<div class="d-flex justify-content-center align-items-center h-100 d-none spinny">
					<div class="spinner-border text-danger" role="status">
						<span class="visually-hidden">Loading...</span>
					</div>
				</div>
				<div id="editor" class="d-none" />
			</main>
			<!-- create a modal that give a signup when clicked on signup -->
			
		</div>
	</div>
</body>

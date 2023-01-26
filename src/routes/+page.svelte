<script>
	// @ts-nocheck

	import { onMount } from 'svelte';
	import Quill from 'quill';
	let quill = null;
	let videoContent = [];
	let promise;
	$: console.log('videoContent', videoContent);

	async function createDocument() {
		var url = document.querySelector('.youtubeUrl').value;
		try {
			var videoId = new URL(url).searchParams.get('v');
			document.querySelector(
				'.card-img-top'
			).src = `https://img.youtube.com/vi/${videoId}/maxresdefault.jpg`;
		} catch (error) {
			alert('Please enter a valid youtube url');
			return false;
		}

		document.querySelector('.spinny').classList.remove('d-none');
		document.querySelector('#cardDiv').classList.add('d-none');
		let container = document.getElementById('editor');
		var myHeaders = new Headers();
		myHeaders.append('Content-Type', 'application/json');
		var requestOptions = {
			method: 'POST',
			headers: myHeaders,
			redirect: 'follow'
		};
		promise = fetch('http://127.0.0.1:5000/getData?url=' + url, requestOptions)
			.then((response) => response.text())
			.then((result) => {
				let data = JSON.parse(result);
				if (data == null) {
					console.log('data is null');
					document.querySelector('#cardDiv').classList.remove('d-none');
					return;
				} else {
					document.querySelector('#title').innerHTML = data['title'];
					document.querySelector('#editor-div').classList.remove('d-none');
				}
				data = data['data'];
				// save data as array in videoContent
				videoContent = Object.values(data);
				console.log('123', videoContent);
				return Object.values(data);
				// for (const [key, value] of Object.entries(data)) {
				// 	console.log(`${key}: ${value}`);
				// 	let string = '<br><div contenteditable="true" class="edit-text">';
				// 	for (const [keys, values] of Object.entries(value)) {
				// 		console.log(`${keys}: ${values}`);
				// 		if (keys == 'heading') {
				// 			string += `<h2>${values}</h2>`;
				// 		}
				// 		if (keys == 'text') {
				// 			string += `<p>${values}</p>`;
				// 		}
				// 	}
				// 	string += '</div><br>';
				// 	// document.querySelector('#renderHere').innerHTML += string;
				// }

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
			background: #ff3801;
			color: white;
			border: 3px solid black;
			border-radius: 0px;
		}

		@media (min-width: 640px) {
			main {
				max-width: none;
			}
		}

		.left-side-bar {
			width: 20%;
			/* make sticky while scrolling */
			position: sticky;
			top: 0;
			/* height: screen height */
			height: 100vh;
		}
		.text-black {
			color: black;
		}

		/* left-side-bar should hide when on mobile mode */
		@media (max-width: 640px) {
			.left-side-bar {
				display: none;
			}
			.right-side-bar {
				padding: 20px !important;
			}

			.getCard {
				height: 450px !important;
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

		.bg-theme-dark {
			bottom: 0;
			border-bottom: 3px solid black;
		}
		.bg-left-grad {
			border-right: 3px solid black;
		}
		.logo-image {
			height: 50px;
			width: 180px;
			object-fit: cover;
		}
		.neo-brutalist-button {
			background-color: #b5ff5b;
			color: black;
			border: none;
			padding: 10px 20px;
			font-size: 16px;
			font-weight: bold;
			text-transform: uppercase;
			letter-spacing: 2px;
			transition: background-color 0.2s ease-in-out;
			margin-right: 15px;
			-webkit-box-shadow: 8px 8px 0px -2px rgba(0, 0, 0, 1);
			-moz-box-shadow: 8px 8px 0px -2px rgba(0, 0, 0, 1);
			box-shadow: 8px 8px 0px -2px rgba(0, 0, 0, 1);
		}
		.neo-brutalist-button:hover {
			background-color: #90b212;
		}

		.banner-image {
			width: 100%;
			-webkit-box-shadow: 8px 8px 0px -2px rgba(0, 0, 0, 1);
			-moz-box-shadow: 8px 8px 0px -2px rgba(0, 0, 0, 1);
			box-shadow: 8px 8px 0px -2px rgba(0, 0, 0, 1);
		}

		.neo-brutalist-button.purple {
			background-color: #873bff;
			color: white;
		}

		.bg-neo-violet {
			background-color: #873bff;
		}
		.w-80 {
			width: 80%;
		}
		.getCard {
			border: 3px solid black;
			border-radius: 0px;
			height: 300px;
		}
		.renderHere {
			border: 3px solid black;
			border-radius: 0px;
			height: 300px;
		}

		.neo-b-input {
			background-color: white;
			color: black;
			border: none;
			padding: 10px 20px;
			font-size: 16px;
			font-weight: bold;
			letter-spacing: 2px;
			transition: background-color 0.2s ease-in-out;
			margin-right: 15px;
			-webkit-box-shadow: 8px 8px 0px -2px rgba(0, 0, 0, 1);
			-moz-box-shadow: 8px 8px 0px -2px rgba(0, 0, 0, 1);
			box-shadow: 8px 8px 0px -2px rgba(0, 0, 0, 1);
		}

		.right-side-bar {
			padding: 0 100px;
		}
		#editor-div {
			border: 3px solid black;
			border-radius: 0px;
			padding: 10px 20px;
		}

		#title {
			background: #b5ff5b;
			font-weight: bold;
			padding: 10px;
			text-align: center;
			letter-spacing: 2px;
			transition: background-color 0.2s ease-in-out;
			margin-right: 15px;
			-webkit-box-shadow: 8px 8px 0px -2px rgb(0 0 0);
			-moz-box-shadow: 8px 8px 0px -2px rgba(0, 0, 0, 1);
			box-shadow: 8px 8px 0px -2px rgb(0 0 0);
		}
		.edit-text {
			padding: 3px;
		}

		.card-img-top {
			width: 130%;
			border: 3px solid black;
			-webkit-box-shadow: 8px 8px 0px -2px rgb(0 0 0);
			-moz-box-shadow: 8px 8px 0px -2px rgba(0, 0, 0, 1);
			box-shadow: 8px 8px 0px -2px rgb(0 0 0);
			margin-left: 10px;
		}
	</style>

	<nav class="navbar navbar-dark bg-theme-dark">
		<span class="navbar-brand p-2">
			<img class="logo-image" src="/wordpilot-variant.png" alt="" width="120" />
		</span>

		<a class="neo-brutalist-button" href="/login">Login</a>
	</nav>

	<div class="d-flex">
		<!-- side bar in the left side in same colour as nav -->
		<div class="bg-left-grad left-side-bar">
			<div class="d-flex flex-column">
				<!-- make the card 20% overflow through the side bar to the other div -->
				<div class="my-5 card m-3">
					<!-- show an youtube thumbnail -->
					<img
						src="https://q5n8c8q9.rocketcdn.me/wp-content/uploads/2019/09/YouTube-thumbnail-size-guide-best-practices-top-examples.png.webp"
						class="card-img-top"
						alt="..."
					/>
				</div>
				<!-- another card saying free for 10 days after please sign in -->
				<div class="my-2 glossy card m-3">
					<!-- <div class="card-header">Note</div> -->
					<div class="card-body">
						<h5 class="card-title text-black">Get Extras</h5>
						<p class="card-text">
							Sign up to get extra features like generating images, audio transpiler and more.
						</p>
						<button class="neo-brutalist-button purple">Register</button>
					</div>
				</div>
			</div>

			<!-- create a card of youtube thumbnail -->
		</div>
		<!-- center the div inside -->
		<div class="d-flex w-100 justify-content-center right-side-bar">
			<div class=" flex-column justify-content-center align-items-center">
				<div id="cardDiv" class="mt-4">
					<h1 class="mt-5">Convert Your Youtube videos to Blog</h1>
					<div class="getCard card bg-neo-violet text-white">
						<div class="card-body h-100 d-flex flex-column flex-md-row">
							<div>
								<img class="banner-image" src="/home-banner.png" alt="" />
							</div>
							<div
								class="input-group mb-3 d-flex flex-column p-2 ml-4 align-items-end justify-content-end"
							>
								<input type="text" class="neo-b-input youtubeUrl w-100" placeholder="Youtube URL" />
								<!-- onclick call the  createDocument function -->
								<button
									class="neo-brutalist-button w-100 mt-2"
									type="button"
									id="button-addon2"
									on:click|once={createDocument}
								>
									Generate
								</button>
							</div>
						</div>
					</div>
					<div class="d-flex justify-content-center align-items-center h-100 d-none spinny">
						<div class="spinner-border text-danger" role="status">
							<span class="visually-hidden">Loading...</span>
						</div>
					</div>
				</div>

				<!-- <div id="renderHere" class="d-none">
						<div id="editor" class="d-none" />  
					</div> -->
				{#if promise}
					<div id="editor-div" class=" mt-4">
						<h1 id="title" class="mt-5" />
						{#await promise}
							Loading...
						{:then contents}
							{#each contents as content}
								<p>hello {content.heading}</p>
							{/each}
						{:catch error}
							{error.message}
						{/await}
					</div>
				{/if}
			</div>
		</div>
	</div>
</body>

<script>
	// @ts-nocheck
	import { onMount } from 'svelte';

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

	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
	<link href="//cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet" />
	<style>
		/* card height 500px */

		.card {
			height: 100%;
		}

		/* poppins font */

		@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap');

		/* font family Poppins for everythong */

		* {
			font-family: 'Jost', sans-serif;
		}
		/* 
		.bg-dark {
			background-color: #28304e !important;
		} */
	</style>
</svelte:head>
<body>
	<section>
		<div class="home">
			landing page
		</div>
	</section>

	<style lang="scss">
		.list {
			margin-top: 100px;
			margin-left: 100px;
			background-color: yellow;
			border:1px solid black;

		}
		.home {
			a {
				color: green;
			}
			p {
				background-color: yellow;
			}
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

		.neo-brutalist-button.purple {
			background-color: #873bff;
			color: white;
		}

		.bg-neo-violet {
			background-color: #873bff;
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

		.neo-title {
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
	</style>
</body>

<script>
	// @ts-nocheck

	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	let videoInput = '';
	let showHome = true;


	async function createDocument() {
		
		var url = videoInput;
		console.log('url', url);
		try {
			var videoId = new URL(url).searchParams.get('v');
			document.querySelector(
				'.card-img-top'
			).src = `https://img.youtube.com/vi/${videoId}/maxresdefault.jpg`;
		} catch (error) {
			alert('Please enter a valid youtube url');
			return false;
		}
		//  router push to video/:id
		goto(`/video/${videoId}`);
	}

	onMount(() => {});

</script>

<body>
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
				{#if showHome}
					<div id="cardDiv" class="mt-4">
						<h1 class="mt-5">Convert Your Youtube videos to Blog</h1>
						<div class="getCard card bg-neo-violet text-white">
							<div class="card-body h-100 d-flex flex-column flex-md-row">
								<div>
									<img class="banner-image" src="/home-banner-0.png" alt="" />
								</div>
								<div
									class="input-group mb-3 d-flex flex-column p-2 ml-4 align-items-end justify-content-end"
								>
									<input
										type="text"
										class="neo-b-input youtubeUrl w-100"
										bind:value={videoInput}
										placeholder="Enter Youtube URL"
									/>
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
					</div>
				{/if}
			</div>
		</div>
	</div>

	<style lang="scss">
		.glossy {
			/*  light pink to purple */
			background: $neo-green;
			color: white;
			border: 3px solid black;
			border-radius: 0px;
		}
		.left-side-bar {
			width: 20%;
			/* make sticky while scrolling */
			position: sticky;
			top: 0;
			/* height: screen height */
			height: calc(100vh - 84.4px);
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
			@extend %neo-box-shadow;

			&:hover {
				opacity: 0.8;
			}
			&.purple {
				background-color: #873bff;
				color: white;
			}
		}

		.banner-image {
			width: 100%;
			@extend %neo-box-shadow;
		}


		.bg-neo-violet {
			background-color: #873bff;
		}
		.getCard {
			@extend %neo-border;
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
			@extend %neo-box-shadow;
		}

		.right-side-bar {
			padding: 0 100px;
		}

		.neo-title {
			background: #b5ff5b;
			font-weight: bold;
			padding: 10px;
			text-align: center;
			letter-spacing: 2px;
			transition: background-color 0.2s ease-in-out;
			margin-right: 15px;
			@extend %neo-box-shadow;
		}
		.card-img-top {
			width: 130%;
			@extend %neo-border;
			@extend %neo-box-shadow;
			margin-left: 10px;
		}

		.loader {
			height: 200px;
			width: 100%;
			object-fit: cover;
		}

		.neo-editor {
			&__ {
				&right {
					margin-left: 20px;
				}

				&left {
					width: 40px;
				}

				&tool {
					padding: 5px;
					margin: 2px;
					border: 2px solid black;
					cursor: pointer;
				}

				&tool.edit:hover {
					background: #5b35c8;
				}

				&tool.screenshot:hover {
					background: #b5ff5b;
				}

				&tool.remove:hover {
					background: #ff3801;
				}

				&icon {
					width: 20px;
				}
			}
		}

	</style>
</body>

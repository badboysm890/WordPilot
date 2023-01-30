<script>
	// @ts-nocheck

	import { onMount } from 'svelte';
	import Quill from 'quill';
	let quill = null;
	let videoId;
	let videoInput = '';
	let videoContent;

	let title = '';
    import { page } from '$app/stores';

	function getNeoHomeElemnet(e) {
		let div = e.target;
		let parent = div.parentNode;
		console.log('div', div);
		console.log('parent', parent);
		console.log('parentNode', parent.parentNode);
		let siblings;
		console.log('parent.parentNode.className', parent.parentNode.className);
		if(parent.parentNode.className.includes('neo-home')) {
			console.log('button clicked');
			siblings = Array.from(parent.parentNode.children);
		} else {
			console.log('image clicked');
			siblings = Array.from(parent.parentNode.parentNode.children);
		}
		return siblings;
	}

	function checkIfEditorExists(neoHomeElement) {
		if (neoHomeElement && neoHomeElement[1].children[1] && neoHomeElement[1].children[1].className.includes('ql-container')) {
			let editor = neoHomeElement[1].children;
			let content = document.createElement('div');
			content.classList.add('neo-editor__right');
			content.innerHTML = editor[1].children[0].innerHTML;
			neoHomeElement[1].replaceWith(content);
			neoHomeElement[1].remove();		
			return true;
		}
	}

	function handleEdit(e, i) {
		let neoHomeElement = getNeoHomeElemnet(e);
		if (checkIfEditorExists(neoHomeElement)) {
			return;
		}
		let editor = document.createElement('div');
		editor.className = 'editor';
		editor.innerHTML = neoHomeElement[1].innerHTML;
		let editorWrapper = document.createElement('div');
		editorWrapper.className = 'neo-editor__right';
		editorWrapper.appendChild(editor);
		neoHomeElement[1].replaceWith(editorWrapper);


		let quill = new Quill(editor, {
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
		// quill.setContents();
		quill.enable();
		quill.focus();
	}

	function handleHide(e, i) {
		let neoHomeElement = getNeoHomeElemnet(e);
		checkIfEditorExists(neoHomeElement)
		 
	}

	async function loadVideoBlog() {
		document.querySelector(
				'.card-img-top'
			).src = `https://img.youtube.com/vi/${videoId}/maxresdefault.jpg`;
		var myHeaders = new Headers();
		myHeaders.append('Content-Type', 'application/json');
		var requestOptions = {
			method: 'POST',
			headers: myHeaders,
			redirect: 'follow'
		};
		let youtubeUrl = `https://www.youtube.com/watch?v=${videoId}`
		videoContent = fetch('http://127.0.0.1:5000/getData?url=' + youtubeUrl, requestOptions)
			.then((response) => response.text())
			.then((result) => {
				let data = JSON.parse(result);
				if (data == null) {
					return;
				} else {
					title = data['title'];
				}
				data = data['data'];
				return Object.values(data);
			})
			.catch((error) => console.log('error', error));
	}

	onMount(() => {
		videoId = $page.params.videoId;
		loadVideoBlog(videoId);
    });

	// remove <pad> and </s> from the string
	function removePAD(str) {
		return str && str.replace(/<pad>/g, '').replace(/<\/s>/g, '');
	}
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
				{#if videoContent}
					{#await videoContent}
						<div class="w-100 h-100 d-flex justify-content-center align-self-center flex-column">
							<h4 class="neo-title">Please be patient, we are generating your content...</h4>
							<img src="/loader.gif" class="loader" alt="" />
						</div>
					{:then contents}
						<div id="editor-div" class=" mt-4">
							<h1 class="my-4 neo-title">{title}</h1>
							{#each contents as content, i (content)}
								<div class="d-flex flex-row neo-editor neo-home">
									<div class="d-flex flex-column neo-editor__left">
										<button on:click|preventDefault={event => handleEdit(event, i)} class="neo-editor__tool edit" ><img class="neo-editor__icon" src="/edittools/edit.png" alt="edit"></button>
										<div class="neo-editor__tool screenshot"><img class="neo-editor__icon" src="/edittools/image.png" alt="screenshot"></div>
										<div class="neo-editor__tool remove"><img class="neo-editor__icon" src="/edittools/trash.png" alt="delete"></div>
									</div>
									<div class="neo-editor__right">
										<h2 class="neo-editor__heading">{removePAD(content.heading)}</h2>
										<p class="neo-editor____text">{content.text}</p>
									</div>

								</div>
								<br />
							{/each}
						</div>
					{:catch error}
						{error.message}
					{/await}
				{/if}
			</div>
		</div>
	</div>

	<style lang="scss">
		.glossy {
			/*  light pink to purple */
			background: $neo-red;
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

					img {
						width: 100%;
					}
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

		.ql {
			&-{
				&editor {
					font-size: 16px;
					font-family: Jost;
					height: 200px;
				}
				&container {
					height: 200px
				}
			}
		}

	</style>
</body>

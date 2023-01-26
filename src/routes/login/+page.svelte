<script>
    let username = "";
    let password = "";

    function handleLogin() {
        // Perform login logic here, such as sending a request to a server
        console.log(`Logging in with username: ${username} and password: ${password}`);
    }
</script>

<form on:submit|preventDefault={handleLogin}>
    <label>
        Username:
        <input type="text" bind:value={username} />
    </label>
    <br />
    <label>
        Password:
        <input type="password" bind:value={password} />
    </label>
    <br />
    <button type="submit">Log in</button>
</form>

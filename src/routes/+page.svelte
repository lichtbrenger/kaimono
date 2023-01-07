<script>
  let items = [];
  let name = "";

  const addItem = () => {
    if(name == '') {
      return;
    }
    items = [
      ...items,
      {
        id: Math.random(),
        name,
      }
    ];
    name = "";
  };

  const remove = item => {
    items = items.filter(i => i !== item);
  };

  const toggle = item => {
    item.done = !item.done;
    items = items;
  };
</script>

<style>
  #bg {
    background: #dccfb9;
    position: fixed; 
    top: 0; 
    left: 0; 

    /* Preserve aspet ratio */
    min-width: 100%;
    min-height: 100%;
  }
  div,
  h1 {
    height: 100%;
    margin: auto;
    color: #dc4f21;
    max-width: 300px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
      Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
  }
  #name {
    width: 100%;
  }
  form {
    margin-bottom: 0.5em;
  }
  input[type="text"] {
    border-radius: 30px;
    background: #efe7db; 
    outline: none;
    margin: 0;
    padding-left: 100px;
    color: #dc4f21;
  }
  input[type="text"]:focus {
    border-color: #dc4f21;
    box-shadow: 0 0 2px #dc4f21;
  }
  input[type="checkbox"] {
    margin: 0 10px 0 0;
  }
  li button {
    float: right;
    border: none;
    background: transparent;
    padding: 0;
    margin: 0;
    color: #dc4f21;
    font-size: 18px;
    cursor: pointer;
  }
  li button:hover {
    transform: scale(2);
  }
  li button:focus {
    outline: #dc4f21;
  }
  li:last-child {
    border-bottom: none;
  }
  label {
    display: block;
    text-transform: uppercase;
    font-size: 0.8em;
    color: #777;
  }
  li {
    list-style: none;
    padding: 6px 10px;
    border-bottom: 1px solid #efe7db;
  }
  ul {
    padding-left: 0;
  }
  span {
    font-size: 36px;
    color: #dc4f21;
  }
  .done span {
    opacity: 0.4;
  }
</style>

<body id='bg'>
<div>
  <h1>買い物</h1>

  <form on:submit|preventDefault={addItem}>
    <label for="name">Add an item</label>
    <input id="name" type="text" bind:value={name} autofocus />
  </form>

  <ul>
    {#each items as item}
      <li class:done={item.done} on:dblclick={() => remove(item)}>
        <span>{item.name}</span>
      </li>
    {/each}
  </ul>
</div>
</body>

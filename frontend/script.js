document.addEventListener('DOMContentLoaded', () => {
    const crearUsuario = document.getElementById('crearUsuario');
    const obtenerUsuarios = document.getElementById('obtenerUsuarios');
    const listaUsuarios = document.getElementById('listaUsuarios');

    crearUsuario.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(crearUsuario);
        const user = {
            username: formData.get('username'),
            email: formData.get('email')
        };

        const response = await fetch('http://127.0.0.1:8000/userdb/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        });

        const result = await response.json();
        alert(`Usuario creado!!👋`);
    });

    obtenerUsuarios.addEventListener('click', async () => {
        const response = await fetch('http://127.0.0.1:8000/userdb/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const users = await response.json();
        listaUsuarios.innerHTML = '';
        users.forEach(user => {
            const li = document.createElement('li');
            li.textContent = `Username: ${user.username}, Email: ${user.email}`;
            listaUsuarios.appendChild(li);
        });
    });
});

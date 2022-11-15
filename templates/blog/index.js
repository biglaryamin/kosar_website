const getUsers = () => {
    axios.get('http://127.0.0.1:8000/blog/articles')
        .then(response =>{
            const articles = response.data;
            console.log("Blogs", articles);
        })
        .catch(error => console.error(error));
};
    getUsers();
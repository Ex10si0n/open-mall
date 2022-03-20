
const Authorization = 'my-token'
// 1. save
export const saveToken = (tokenObj) => {
  localStorage.setItem(Authorization, JSON.stringify(tokenObj))  
}
 
// 2. get
export const getToken = () => {
  return JSON.parse(localStorage.getItem(Authorization))
}
 
// 3. delete
export const delToken = () => {
  localStorage.removeItem(Authorization)
}
import axios from 'axios'
import Cookies from 'js-cookie';
import {toast} from 'react-toastify';

const baseURL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8080';

const instance = axios.create({
    timeout: 10000
});

async function doGet(...args) {
    const resp = await instance.get(...args).catch((error) => {
        if (error.response) {
            toast.error(`${error.response.status}: ${error.response.data.message || error.response.data}`);
        } else {
            toast.error(error.message);
        }
        return null;
    });
    if (resp) {
        return resp.data
    }
    return null;
}

async function doPost(...args) {
    const resp = await instance.post(...args).catch((error) => {
        if (error.response) {
            toast.error(`${error.response.status}: ${error.response.data.message || error.response.data}`);
        } else {
            toast.error(error.message);
        }
        return null;
    });
    if (resp) {
        return resp.data
    }
    return null;
}

async function doPut(...args) {
    const resp = await instance.put(...args).catch((error) => {
        if (error.response) {
            toast.error(`${error.response.status}: ${error.response.data.message || error.response.data}`);
        } else {
            toast.error(error.message);
        }
        return null;
    });
    if (resp) {
        return resp.data
    }
    return null;
}

async function doDelete(...args) {
    const resp = await instance.delete(...args).catch((error) => {
        if (error.response) {
            toast.error(`${error.response.status}: ${error.response.data.message || error.response.data}`);
        } else {
            toast.error(error.message);
        }
        return null;
    });
    if (resp) {
        return resp.data
    }
    return null;
}


export async function getStats() {
    const queryUrl = `${baseURL}/stats`;
    return doPost(queryUrl);
}



export const getImageUrl = (image_rel_url) => (`${baseURL}${image_rel_url}`);
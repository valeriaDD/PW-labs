import axios from 'axios';

const token = "5d98f8bafbecc2328fbc24bc63fe400257844e2bd0c1a5340305ac04ef4b284f";

class HttpClient {
    constructor(baseURL) {
        this.client = axios.create({
            baseURL: baseURL,
            headers: {
                common: {
                    'X-Access-Token': token,
                },
            },
        });
    }

    async get(url, params) {
        try {
            const response = await this.client.get(url, { params });
            return response.data;
        } catch (error) {
            this.handleError(error);
        }
    }

    async post(url, data) {
        try {
            const response = await this.client.post(url, {data: data});
            return response.data;
        } catch (error) {
            this.handleError(error);
        }
    }

    async put(url, data) {
        try {
            const response = await this.client.put(url, data);
            return response.data;
        } catch (error) {
            this.handleError(error);
        }
    }

    async delete(url) {
        try {
            const response = await this.client.delete(url);
            return response.data;
        } catch (error) {
            this.handleError(error);
        }
    }

    handleError(error) {
        console.log('An error occurred:', error);
    }
}

const httpClient = new HttpClient('https://late-glitter-4431.fly.dev/api/v54');

export default httpClient;

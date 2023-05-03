import axios from 'axios';

class HttpClient {
    constructor(baseURL) {
        const token = '176687918888c30addfa5b2e7e21dd6627221005dfedb44f7d17d3c7e2254e8a';
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
        const response = await this.client.get(url, {params});
        return response.data;
    }

    async post(url, data) {
        const response = await this.client.post(url, {data: data});
        return response.data;
    }

    async put(url, data) {
        const response = await this.client.put(url, data);
        return response.data;
    }

    async delete(url) {
        const response = await this.client.delete(url);
        return response.data;
    }

}

const httpClient = new HttpClient('https://late-glitter-4431.fly.dev/api/v54');

export default httpClient;

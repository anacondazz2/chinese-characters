import axios from 'axios';

export const fetchLookupResults = async (query) => {
    try {
        const response = await axios.get(`http://127.0.0.1:8000/api/lookup-entry/?query=${encodeURIComponent(query)}`);
        return response.data;
    }
    catch (error) {
        console.error("Error fetching data:", error);
        return [];
    }
};
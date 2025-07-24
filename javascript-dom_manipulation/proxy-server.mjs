// proxy-server.mjs
import express from 'express';
import cors from 'cors';
import fetch from 'node-fetch';

const app = express();
app.use(cors());

app.get('/api/hello', async (req, res) => {
  try {
    const lang = req.query.lang || 'fr';
    const response = await fetch(
      `https://api.mymemory.translated.net/get?q=Hello!&langpair=en|${lang}`
    );
    const json = await response.json();
    res.json({ hello: json.responseData.translatedText });
  } catch (err) {
    console.error('[SERVER ERROR]', err);
    res.status(500).json({ error: 'Failed to fetch translation' });
  }
});

app.listen(3000, () => {
  console.log('✅ Proxy server running at http://localhost:3000');
});

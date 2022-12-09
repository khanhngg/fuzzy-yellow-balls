import { connection } from '$lib/db'
import type { RequestHandler } from '@sveltejs/kit'

export const POST: RequestHandler = async ({ request }) => {
    const db = await connection()
    const match: string = await request.json()

    console.log({ match });

    const [rows] = await db.execute(`SELECT * FROM serve_influence WHERE match_id=?`, [match])

    // console.log(rows.filter(row => row['set'] === 'Total'));

    return new Response(JSON.stringify(rows))
}
import { connection } from '$lib/db'
import type { RequestHandler } from '@sveltejs/kit'

export const POST: RequestHandler = async ({ request }) => {
    const db = await connection()
    const matches: string[] = await request.json()

    console.log({ matches });

    const [rows] = await db.execute(`SELECT * FROM return_outcome WHERE match_id IN (${Array(matches.length).fill('?').join(',')})`, matches)

    // console.log(rows.filter(row => row['set'] === 'Total'));

    return new Response(JSON.stringify(rows))
}
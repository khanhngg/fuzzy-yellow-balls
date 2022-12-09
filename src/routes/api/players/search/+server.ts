import { connection } from '$lib/db'
import type { RequestHandler } from '@sveltejs/kit'

export const GET: RequestHandler = async ({ url }) => {
    const db = await connection()
    const input = `%${url.searchParams.get('input')}%`

    console.log({ input });

    const [rows] = await db.execute(`SELECT DISTINCT player FROM player_stats WHERE player LIKE ?`, [input])

    // console.log(rows.filter(row => row['set'] === 'Total'));

    return new Response(JSON.stringify((rows as { player: string }[]).map(value => value.player)))
}
import { connection } from '$lib/db'
import type { RequestHandler } from '@sveltejs/kit'

export const POST: RequestHandler = async ({ request }) => {
    const db = await connection()
    const { player } = await request.json()

    const [rows] = await db.execute(`SELECT * FROM player_stats WHERE player = ?`, [player])

    return new Response(JSON.stringify(rows))
}
import type { PageLoad } from './$types';
export const prerender = true;

export const load: PageLoad = async () => {
    const atp = await import('$lib/data/rankings_atp/atp_rankings_all.json');
    const wta = await import('$lib/data/rankings_wta/wta_rankings_all.json');
    return { atp: atp.default, wta: wta.default };
};
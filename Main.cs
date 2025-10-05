using HarmonyLib;
using Verse;

namespace twcyz
{
    [StaticConstructorOnStartup]
    public static class Main
    {
        static Main()
        {
            var harmony = new Harmony("rimworld.twc.yz");
            harmony.PatchAll();
        }
    }
}
